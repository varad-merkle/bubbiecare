import base64
import io

import aiofiles
# from PyPDF2 import PdfReader
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update

from pdfminer.high_level import extract_text
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware

from database import get_db
from embedding_helper import get_resume_embedding, get_jd_embedding, score_resumes_against_jd
from llm_helper import make_json_from_resume_extract, classify_candidate_skills, CandidateProfile, JobDescription, CandidateStatus, OptionsSelected, check_answer
from model import CandidateResume, Options

from send_email import send_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
)

cache = []

@app.post("/extract_attribute_from_resume/")
async def extract_resume_attributes(
        file: UploadFile = File(...),
        db: AsyncSession = Depends(get_db)
):
    # file = client.files.create(file = open("file.pdf", "rb"), purpose="user_data")
    # async with aiofiles.open("file.pdf", 'wb') as out_file:
    #     content = await file.read()
    #     await out_file.write(content)
    # base64_string = base64.b64encode(data).decode("utf-8")

    # Parse the PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Uploaded file is not a PDF")
    contents = await file.read()
    pdf_stream = io.BytesIO(contents)
    # with open(name, "rb") as f:
    #     text = extract_text(f)
        # for page in pdf.pages:
        #     text += page.extract_text()

    try:
        text = extract_text(pdf_stream)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse the PDF - {str(e)}")

    # contents = await file.read()
    # print(contents)
    print(text)
    # print("len: ", len(page.get_contents().get_data()))

    profile = make_json_from_resume_extract(text)
    skills = classify_candidate_skills(profile.skills, profile.experiences)
    embeds = get_resume_embedding(text)

    result = {**profile.model_dump(), **skills.model_dump(), "feature_vector": embeds.tolist()}

    await insert_candidate_profile(result, db)

    return result

    # print(out_file)

    # resume = client.files.create(file=open("file.pdf", "rb"), purpose="user_data")

    # filename = file.filename
    # content_type = file.content_type

    # response = client.responses.create(
    #     model="gpt-5.6-luna",
    #     input=[
    #         {
    #             "role": "user",
    #             "content": [
    #                 {
    #                     "type": "input_file",
    #                     "file_id": resume.id,
    #                     # "filename": "draconomicon.pdf",
    #                     # "file_data": f"data:application/pdf;base64,{base64_string}",
    #                 },
    #                 {
    #                     "type": "input_text",
    #                     "text": "Summarise the file",
    #                 },
    #             ],
    #         },
    #     ],
    # )

    # print(response.output_text)

@app.post("/get_relevant_resumes/")
async def get_relevant_resumes(
        jd: JobDescription,
        db: AsyncSession = Depends(get_db)
):
    global cache
    print(f"cache - {cache} and len - {len(cache)}")
    if jd.job_description is None and len(cache) == 0:
        raise HTTPException(status_code=400, detail="No job description provided")
    # elif jd.job_description is None and len(cache) > 0:
    #     return cache["top_resumes"]
    if len(cache) == 0:
        resumes = await get_all_resumes(db)
        jd_embeds = get_jd_embedding(jd.job_description)
        top_resume_matches = score_resumes_against_jd(resumes, jd_embeds)
    else:
        top_resume_matches = cache
    top_resumes = []
    for resume_id, score in top_resume_matches:
        resume = await get_resume_by_id(db, resume_id)
        resume = resume.scalar()
        res_dict = {"candidate_id": resume, "status": resume.status, "likelyhood": score, "testscore": resume.testscore}
        top_resumes.append(res_dict)
    cache = top_resume_matches
    return {"data": top_resumes}

@app.post("/approve_or_reject/")
async def handle_approve_or_reject(
        candidate_status: CandidateStatus,
        db: AsyncSession = Depends(get_db)
):
    resume = await get_resume_by_id(db, candidate_status.id)
    res = resume.scalar()
    candidate_id = res.id
    name = res.name
    email = res.email
    if candidate_status.status == "approved":
        if email:
            send_email(candidate_id, name, email)
            await update_status(db, candidate_id, "Test Sent")
            return {"data": f"email successfully sent to {email}"}
        else:
            raise HTTPException(status_code=400, detail="Email not found")
    elif candidate_status.status == "interview scheduled":
        await update_status(db, candidate_id, "Interview Scheduled")
        send_email(candidate_id, email, f"Congratulations {name}!You have cleared the screening test and are through to an interview. You should receive a call from a recruiter with the interview schedule details.Thank you, Team BubbieCare")
        return {"data": f"Interview has been scheduled for {name} and an email has been sent."}
    elif candidate_status.status == "reject":
        await update_status(db, candidate_status.id, "Rejected")
        return {"status": "Rejected"}
    return None

@app.post("/getname/")
async def get_name(id: int = Body(..., embed=True), db: AsyncSession = Depends(get_db)):
    resume = await get_resume_by_id(db, id)
    res = resume.scalar()
    return {"name": res.name, "test_status": res.testscore is not None}

answers = {
    "q1": "A",
    "q2": "B",
    "q3": "C"
}

@app.post("/submit_answers/")
async def submit_answers(
        options: OptionsSelected,
        db: AsyncSession = Depends(get_db)
):
    if options.q1 == answers["q1"]:
        m1 = 10
    else:
        m1 = 0
    if options.q2 == answers["q2"]:
        m2 = 10
    else:
        m2 = 0
    if options.q3 == answers["q3"]:
        m3 = 10
    else:
        m3 = 0

    m4: int = int(check_answer("What methods do you use to track and report blood sugar and blood pressure readings to ensure accurate communication with the healthcare provider?", options.q4))
    print(f"m4 = {m4} - {type(m4)}")
    m5: int = int(check_answer("How do you handle situations where the patient refuses to take medications or follow a prescribed routine?", options.q5))
    print(f"m5 = {m5} - {type(m5)}")
    avg_score = (m1+m2+m3+m4+m5)/5.0

    options_with_marks = {**options.model_dump(by_alias=True), "m1": m1, "m2": m2, "m3": m3, "m4": m4, "m5": m5}
    await insert_options_selected(db, options_with_marks)
    await update_status(db, options.id, "test submitted")
    await update_score(db, options.id, avg_score)
    print(options.model_dump(by_alias=True))
    return {"test_status": "Submitted"}

@app.post("/get_answers/")
async def get_answers(id: int = Body(..., embed=True), db: AsyncSession = Depends(get_db)):
    options_record = await db.get(Options, id)
    candidate_record = await db.get(CandidateResume, id)

    return {
        "name": candidate_record.name,
        "marks": {
            "id": id,
            "candidate_id_id": options_record.test_id,
            "q1": options_record.q1,
            "q2": options_record.q2,
            "q3": options_record.q3,
            "q4": options_record.q4,
            "q5": options_record.q5,
            "m1": options_record.m1,
            "m2": options_record.m2,
            "m3": options_record.m3,
            "m4": options_record.m4,
            "m5": options_record.m5,
        }
    }

async def insert_candidate_profile(
        profile: dict,
        db: AsyncSession
):
    await db.execute(insert(CandidateResume).values(profile))
    await db.commit()

async def get_all_resumes(
        db: AsyncSession
):
    resumes = await db.execute(select(CandidateResume.id, CandidateResume.feature_vector))
    return resumes

async def get_resume_by_id(
        db: AsyncSession,
        resume_id: int
):
    resume = await db.execute(select(CandidateResume).where(CandidateResume.id==resume_id))
    return resume

async def update_status(
        db: AsyncSession,
        resume_id: int,
        new_status: str
):
    if new_status == "Rejected":
        resume = await db.execute(update(CandidateResume).where(CandidateResume.id==resume_id).values(status=new_status))
        await db.commit()
        print(f"resume with {resume_id} has been rejected")
    else:
        resume = await db.execute(update(CandidateResume).where(CandidateResume.id==resume_id).values(status=new_status))
        await db.commit()
async def insert_options_selected(
        db: AsyncSession,
        options: dict
):
    await db.execute(insert(Options).values(options))
    await db.commit()

async def update_score(
        db: AsyncSession,
        id: int,
        score: float
):
    updated_candidate_record = await db.execute(update(CandidateResume).where(CandidateResume.id==id).values(testscore=score))
    await db.commit()
    print(f"score updated for {id}")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
