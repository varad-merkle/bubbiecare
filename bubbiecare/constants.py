PARSE_INSTRUCTION = """
Given a string containing resume details.
Extract the resume information and map it into the schema given by CandidateProfile.

Fields such as name, email, phone, location map simply and cleanly.
For certification or education, extract the degree pursued by the individual. Do not extract the location of the university, just the degree or certification.
For total years of experience, calculate the number by considering the difference between the present year and the year of starting a job.
For experiences, each experience can be identified by the designation, duration of work in years, and important points about the job performed. Extract only the job title, duration - as mentioned, and location, if available.
For professional summary, extract it in third person summarising any & all useful information about the candidate.
"""
MODEL = "gpt-5.6-luna"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
RETRIEVAL_MODEL = "multi-qa-MiniLM-L6-dot-v1"
CLASSIFICATION_INSTRUCTION = """
Given a string a care giver candidate's skills and experiences, assign a boolean value to the following 4 variables:
1. companion_care - conversation & social interaction, driving to appointments & social events, escorting to religious services, assistance with hobbies, tech support, memory games & cognitive stimulation, accompaniment on walks or outings 
2. personal_care - bathing & showering, dressing & grooming, toileting & incontinence care, oral hygiene & denture care, shaving & hair care, assistance with transfers (bed to chair), ambulation & walking support, feeding assistance, repositioning for bedbound clients
3. respite_care - 24-hour live-in care, overnight supervision, respite care for family caregivers, hospital to home transition support, hospice support & comfort care, dementia & alzheimer's redirecting, travel companionship & assistance
4. hospice_care - a combination of all attributes mentioned above and household & lifestyle support, medication reminders, vital sign tracking, blood glucose monitoring assistance, fall prevention & stand-by assistance, range of motion exercises, physical therapy follow-through, medical appointment scheduling, incision or wound observation

The skills and experiences should determine whether the candidate can be classified as qualified enough to demonstrate each of the 4 skills.
"""

software_resume_text = """ANIK KUMAR BISWAS 
Senior Software Engineer | Python | Generative AI | Agentic AI | LLM Orchestration | Backend & Cloud 
anikece5010@gmail.com | +91 93828 15887 | Bangalore, India | https://www.linkedin.com/in/anik-biswas-430b7a15a/ | https://github.com/Anik-
1997-Biswas 

PROFESSIONAL SUMMARY 

Senior Software Engineer with 5+ years building production-grade Python backend systems and Generative AI / Agentic AI solutions for 
global investment banking clients, including Citibank and UBS. Hands-on experience with LLM orchestration (LangChain, LangGraph), 
multi-agent architectures, Model Context Protocol (MCP), and Retrieval-Augmented Generation (RAG), delivered as FastAPI/Flask 
microservices on Azure and GCP. Skilled in prompt engineering, vector database integration (FAISS, ChromaDB), and applying both 
Azure OpenAI and Anthropic Claude models for reasoning, summarization, and decision-support tasks. Strong track record of reducing 
manual effort and deployment time across reconciliation, compliance, and underwriting workflows in high-stakes BFSI environments, 
with a growing focus on human-in-the-loop, observable, production-oriented AI systems. 

CORE COMPETENCIES 

•  Languages & Backend: Python (asyncio, pydantic, SQLAlchemy, pytest, Pandas, NumPy), FastAPI, Flask, REST APIs, SQL 
•  GenAI / Agentic AI: LLMs, Agentic AI, Multi-Agent Orchestration, LangChain, LangGraph, Model Context Protocol (MCP), Azure 

OpenAI, Anthropic Claude / Claude Haiku 4.5, Ollama, Local LLM Inference (Qwen), Prompt Engineering (zero-shot, few-shot, CoT, 
function calling) 

•  RAG & Vector Databases: Retrieval-Augmented Generation, FAISS, ChromaDB, Semantic Search, Embeddings 
•  Microservices & Cloud: Microservices Architecture, Docker, Kubernetes, Azure AI / Azure OpenAI Service, GCP (Vertex AI, Agent 

Runtime, Cloud Run, Cloud SQL), AWS (basic), CI/CD (Jenkins) 

•  Observability & Security: Prometheus, Grafana, AppDynamics, Cloud Monitoring, Braintrust, IAM/RBAC, Okta, Data Masking, 

Schema Validation, AI Governance 

•  Database & ORM: Oracle, Snowflake, PL/SQL, SQLAlchemy, RDBMS Administration 
•  Banking / Finance Domain: Reconciliation Automation, AML Compliance, Retail Lending, SFTR, DTCC, SDRA, Regulatory Reporting, 

Trade Validation 

•  Tools: Streamlit, AutoSys, CRON, Gresham CTC, Git, Unix/Linux Shell Scripting 

WORK EXPERIENCE 

Senior Software Engineer — AI & Cloud  |  Virtusa | Citibank 
•  Integrated GitHub Copilot and ChatGPT APIs into daily banking development workflows using Python, cutting code 

Mar 2025 – Present 

authoring/review time by ~35% via AI-assisted code generation, documentation, and test creation. 

•  Built AI-enabled Python applications on Azure OpenAI Service (GPT-4) for intelligent document summarization, semantic search, 

and automated compliance report generation. 

•  Designed and deployed multi-agent AI systems using LangChain, LangGraph, and Ollama to automate banking workflows via async 

Python APIs integrated with Azure OpenAI, cutting processing time by ~40%. 

•  Adopted Model Context Protocol (MCP) to standardize LLM agent access to enterprise tools; built a Python MCP orchestrator 

coordinating multiple MCP clients/servers, exposing banking systems (databases, APIs, document stores) as reusable, tool-aware 
MCP servers. 

•  Built production RAG pipelines with FAISS and ChromaDB for semantic search over enterprise knowledge bases, deployed as 

FastAPI microservices for instant SOP retrieval. 

•  Engineered scalable REST APIs with FastAPI and Flask, containerized with Docker and Kubernetes, ensuring 99.9% uptime for critical 

financial systems. 

•  Delivered AI-driven reconciliation and AML automation platforms on GCP (Vertex AI, Agent Runtime, Cloud Run, Cloud SQL, Load 

Balancers) and Azure AI, eliminating ~60% of manual review effort. 

•  Implemented monitoring/observability with Prometheus, Grafana, Cloud Monitoring, and Braintrust for agent/LLM metrics, driving 

a ~35% reduction in MTTR. 

•  Owned production AI agent lifecycle — LLM evaluations, model/version upgrades, and platform security protocols — and 

configured Okta authentication, IAM/RBAC access, data masking, and schema validation across AI-enabled banking applications. 

Senior Associate — Software Developer  |  Atyeti IT Services | UBS Bank 
•  Led reconciliation automation for Credit Suisse regulatory projects across UK, US, and Poland as part of a global client-facing 

Nov 2020 – Feb 2025 

support team, building Python services covering SDRA, DTCC, GSL, and SFTR compliance. 

•  Automated batch monitoring, data validation, and anomaly detection pipelines using Python and Shell scripting on Linux/Unix, 

reducing manual intervention by ~50%. 

•  Provided L2/L3 production support and root cause analysis (RCA) across multiple banking applications in a high-volume financial 

institution environment, consistently meeting SLA targets. 


•  Managed ETL pipelines across Oracle and Snowflake; optimized SQL queries via Python-driven jobs, improving data throughput by 

~30%, using Gresham CTC and AutoSys/CRON-based job scheduling. 

KEY PROJECTS 

Project LUNA — GenAI Banking Agent Assist 
Python, FastAPI, PostgreSQL, SQLAlchemy, Ollama/Qwen, Docker 
•  Built a GenAI Agent Assist solution for banking customer-service workflows using FastAPI, PostgreSQL, and a locally hosted Qwen 

model served via Ollama, giving service representatives contextual assistance drawn from customer and transaction data instead of 
manual lookups across multiple systems. 

•  Developed a Customer 360 context engine with SQLAlchemy to retrieve customer, account, card, and transaction data and inject 

relevant context into controlled LLM prompts. 

•  Implemented PostgreSQL-backed conversation memory for customer/AI/agent interactions and designed contextual response 

generation that combines LLM output with deterministic business-action recommendations (e.g., flagging pending transactions for 
verification). 

•  Built on a modular architecture with dependency injection, transaction handling, local LLM inference, and containerized 

deployment via Docker — designed to be extended with RAG, LangGraph-based agents, tool calling, guardrails, and human-in-the-
loop approval. 

AI-Powered Retail Lending Decision & Underwriting Platform (Proof-of-Concept) 
•  Designed and built a proof-of-concept agentic loan-decisioning workflow in Python/FastAPI, decomposing underwriting into 

6 months 

specialized functional agents — Customer Profile, Credit Risk, Repayment Capacity, Payment Status, Policy/Eligibility, Decision, and 
Explainability — coordinated through an orchestrated, LangGraph-based workflow rather than ad-hoc calls. 

•  Implemented deterministic underwriting logic (FOIR calculation, repayment capacity, eligibility rules) as modular Python services 

and ML-based risk/credit scoring, keeping financial calculations and predictions separate from the GenAI reasoning layer. 
•  Used Claude Haiku 4.5 for contextual reasoning and decision explanation — summarizing applicant context and translating 

model/rule outputs into underwriter-readable rationale — never for the underlying financial calculations themselves. 

•  Exposed banking, customer, and payment-status data through an MCP client-server architecture, giving agents standardized, tool-

aware access to underwriting data sources. 

•  Built a maker-checker approval workflow with full audit trail and human-in-the-loop sign-off before any lending decision was 

finalized; used Python/Faker to generate synthetic test datasets for evaluation. 

•  Delivered a Streamlit dashboard for portfolio KPIs, underwriting summaries, and audit trails; applied IAM-based RBAC and data 

masking across the pipeline in line with AI governance guidelines. 

Citi Bank Financial Data Store — AI-Enabled Enterprise Platform  —  Citibank 
•  Architected an enterprise data platform integrating Python, FastAPI, SQL, and ETL pipelines with GenAI-powered workflow 

18 months 

automation; embedded Azure OpenAI and LangChain-based LLM components for intelligent reconciliation, anomaly detection, and 
incident resolution — reducing manual effort by ~55%. 

•  Designed an MCP-based integration layer with a central MCP orchestrator coordinating MCP clients and servers, letting LLM agents 

securely call the financial data store, ETL pipelines, and reconciliation tools as standardized, discoverable tools. 

•  Integrated GitHub Copilot for AI-assisted Python development; enforced data/schema validation with IAM/RBAC access controls 

and data masking safeguarding sensitive financial data. 

Gresham UBS IB Reconciliation — Credit Suisse  —  UBS Bank 
36 months 
•  Delivered end-to-end regulatory reconciliation across UK, US, and Poland using Python, Shell scripting, and SQL; supported SDRA, 

DTCC, GSL, and SFTR compliance with automated matching, anomaly detection, and full RCA documentation. 

EDUCATION 

B.Tech / B.E. — Dr. BC Roy Engineering College, Durgapur — 2020 

CERTIFICATIONS & TRAINING 

•  Generative AI — Virtusa (Internal Certification) 
•  Java, SQL & Web Technologies — JSpiders Academy 

ADDITIONAL INFORMATION 

Open to rotational shift work and global client-facing support engagements. """

healthcare_resume_text = """Contact Information 

Name: Michael Roberts 
Email: michael.roberts@yopmail.com 
Phone: +91-9876512345 
Location: Pune, India 

Professional Summary 

Dedicated healthcare professional with experience in general patient care and administrative support. 
Strong background in assisting medical staff, maintaining patient records, and ensuring smooth clinic 
operations. Looking to transition into a nursing role with a focus on patient care. 

Education 

  Diploma in Healthcare Administration, Pune Institute of Medical Sciences – 2018 

Work Experience 

Medical Office Assistant 

City Health Clinic, Pune (2020 – Present) 

  Assisted in patient scheduling and medical record management. 

  Provided basic first-aid support to patients. 

  Managed administrative tasks to support medical professionals. 

Front Desk Executive 

Wellness Medical Center, Pune (2018 – 2020) 

  Greeted patients and coordinated appointments. 

  Handled patient queries and maintained records. 

Key Skills 

  Patient Coordination 

  Medical Administration 

 

First Aid Assistance 

  Record Management 

 
 
 
 

  Communication Skills 

Work Preferences 

  Open to roles in healthcare administration or patient support. 

  Willing to gain knowledge in clinical support roles. 

Languages 

  English (Fluent) 

  Hindi (Fluent) """