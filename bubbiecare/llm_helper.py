import os
import requests
from openai import OpenAI
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from openai import AzureOpenAI
from load_dotenv import load_dotenv

from constants import PARSE_INSTRUCTION, MODEL, CLASSIFICATION_INSTRUCTION

load_dotenv()

BASE_URL = os.getenv("GATEWAY_BASE_URL", "https://ai-api-dev.dentsu.com")
SUB_KEY = os.getenv("OPENAI_SUBSCRIPTION_KEY")
BRAND = os.getenv("X_BRAND", "dentsu")
SERVICE_LINE = os.getenv("X_SERVICE_LINE", "creative")
PROJECT = os.getenv("X_PROJECT", "playground-test")

def get_bearer_token() -> str:
    """Exchange subscription key for a Bearer JWT."""
    resp = requests.post(
        f"{BASE_URL}/token/retrieve",
        headers={
            "Ocp-Apim-Subscription-Key": SUB_KEY,
            "api-version": "v1",
            "x-brand": BRAND,
            "x-service-line": SERVICE_LINE,
            "x-project": PROJECT
        }
    )
    resp.raise_for_status()
    return resp.json()["access_token"]

token = get_bearer_token()

# client = OpenAI()
# client = genai.Client()

client = OpenAI(
    api_key="not needed",
    base_url=f"{BASE_URL}/openai/v1",
    default_headers={
        "Ocp-Apim-Subscription-Key": SUB_KEY,
        "Authorization": f"Bearer {token}",
        "x-brand": BRAND,
        "x-service-line": SERVICE_LINE,
        "x-project": PROJECT
    }
)

class CandidateProfile(BaseModel):
    name: str
    email: str
    location: str
    skills: str
    certifications: str
    total_experience: int
    experiences: str
    summary: str

class CandidateSkills(BaseModel):
    companion_care: bool
    personal_care: bool
    respite_care: bool
    hospice_care: bool

class JobDescription(BaseModel):
    job_description: str | None

class CandidateStatus(BaseModel):
    id: int
    status: str

class OptionsSelected(BaseModel):
    id: int = Field(serialization_alias="test_id")
    q1: str
    q2: str
    q3: str
    q4: str
    q5: str

def make_json_from_resume_extract(resume_text: str) -> CandidateProfile:
    response = client.responses.parse(
        input = [
            {"role": "system", "content": PARSE_INSTRUCTION},
            {"role": "user", "content": resume_text},
        ],
        model=MODEL,
        text_format=CandidateProfile
    )

    # response = client.interactions.create(
    #     model="gemini-3.8-flash",
    #     system_instruction=PARSE_INSTRUCTION,
    #     input=resume_text,
    #     response_format={
    #         "type": "text",
    #         "mime_type": "application/json",
    #         "schema": CandidateProfile.model_json_schema()
    #     }
    # )

    # candidate_profile = response.output_parsed
    candidate_profile = CandidateProfile.model_validate_json(response.output_text)
    return candidate_profile

def classify_candidate_skills(skills: str, experiences: str) -> CandidateSkills:
    response = client.responses.parse(
        input = [
            {"role": "system", "content": CLASSIFICATION_INSTRUCTION},
            {"role": "user", "content": f"skills - {skills} \n experiences - {experiences}"},
        ],
        model=MODEL,
        text_format=CandidateSkills
    )

    # response = client.interactions.create(
    #     input = f"skills - {skills} \n experiences - {experiences}",
    #     system_instruction=CLASSIFICATION_INSTRUCTION,
    #     model="gemini-3.8-flash",
    #     response_format={
    #         "type": "text",
    #         "mime_type": "application/json",
    #         "schema": CandidateSkills.model_json_schema()
    #     }
    # )

    # candidate_skills = response.output_parsed
    candidate_skills = CandidateSkills.model_validate_json(response.output_text)
    print(candidate_skills)
    return candidate_skills

def check_answer(question: str, answer: str) -> int:
    response = client.responses.parse(
        input = [
            {"role": "system", "content": f"For the given question - {question} check how accurate the provided answer is and"
                                          f"assign a score on a scale of 0 to 10, where 0 is the least and 10 is the highest. Only"
                                          f"return the actual score as an integer, i.e. a number between 0 and 10, nothing else"},
            {"role": "user", "content": f"user provided answer to the question = {answer}"},
        ],
        model=MODEL
    )

    return response.output_text