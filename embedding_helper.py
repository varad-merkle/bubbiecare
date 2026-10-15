from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer

from constants import EMBEDDING_MODEL, RETRIEVAL_MODEL

# Load a pre-trained transformer model
model = SentenceTransformer(f'sentence-transformers/{RETRIEVAL_MODEL}')
# tokenizer = model.tokenizer

jd_text = """Job Title: Male Diabetes Care Specialist Location: California 

Job Type: Full-Time 

About Us: We are a dedicated healthcare team committed to enhancing the quality of life for older adults managing diabetes. We are seeking a compassionate and highly skilled Male Diabetes Care Specialist to join our team. 

Position Overview: As a Diabetes Care Specialist, you will play a crucial role in 

supporting older adults with diabetes. You will collaborate with an interdisciplinary healthcare team to create individualized care plans, provide patient education, and develop geriatric-focused resources. Your efforts will help promote healthy living and improve the overall well-being of our senior patients. 

Key Responsibilities: 

Develop and implement individualized care plans, including glucose monitoring, medication management, and stress-reduction techniques. 

Conduct patient education sessions tailored to seniors and their families. 

Create and distribute geriatric-focused resources. 

Coordinate social media campaigns to promote healthy living. 

Engage in proactive community outreach to empower senior patients to adopt sustainable lifestyle changes. 

Qualifications: 

Bachelor of Science in Nursing (BSN). 

Valid Certified Nursing Assistant (CNA) certification. 

Basic Life Support (BLS) certification. 

Certified Diabetes Care and Education Specialist (CDCES) credential. 

Strong communication and interpersonal skills. 

Commitment to continuous learning and professional development. 

Why Join Us: 

Make a meaningful impact on the lives of older adults. 

Work with a supportive and interdisciplinary healthcare team. 

Engage in innovative and community-focused healthcare initiatives. """

def get_resume_embedding(resume: str):
    embeddings = model.encode(resume)
    # tokens = tokenizer.encode(resume)
    # tokens_jd = tokenizer.encode(jd_text)
    # print(f"JD Tokens: {len(tokens_jd)}")
    # print(f"Tokens: {len(tokens)}")
    # return embeddings.tolist()
    print(embeddings.shape)
    # print(embeddings.tolist())
    return embeddings

def get_jd_embedding(jd: str) -> list[float]:
    embeddings = model.encode(jd)
    print(f"JD shape: {embeddings.shape}")
    return embeddings.tolist()

def score_resumes_against_jd(resumes, jd_embeds):
    sorted_resume_ids = []
    feature_vectors = []
    ids = []
    for resume in resumes:
        ids.append(resume.id)
        feature_vectors.append(resume.feature_vector)
    # print(resume)
    score = util.dot_score(jd_embeds, feature_vectors)[0].cpu().tolist()
    print(score)
    doc_score_pairs = list(zip(ids, score))
    return doc_score_pairs
    # doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
    # for doc, score in doc_score_pairs:
    #     sorted_resume_ids.append(doc)
    #     print(f"Type of doc id: {type(doc)}")
    #     print(score, doc)
    # return sorted_resume_ids
    # print(scores)