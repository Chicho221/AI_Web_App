from fastapi import FastAPI
from analyzer import analyze_job, analyze_jobFake
from pydantic import BaseModel
import pydantic
app = FastAPI()
history = []

class JobRequest(BaseModel):
    title: str
    company:str

@app.get("/history")
def get_history():
    return history

@app.get('/')
def home():
    return {'message': 'AI Job Analyzer API is running'}

# POST Analysis
@app.post("/analyze")
def analyze_post(job: JobRequest):
    result = analyze_jobFake(job.model_dump())

    history.append({
        "job": job.model_dump(),
        "result": result
    })
    return {"analysis": result}

# GET Analysis
@app.get("/analyze")
def analyze(title: str, company: str):

    job = {
        "title": title,
        "company": company
    }

    result = analyze_jobFake(job)

    return{
        "analysis": result
    }

# Analyze using AI
@app.get("/analyzeAI")
def analyze(title: str, company: str):

    job = {
        "title": title,
        "company": company
    }

    result = analyze_job(job)

    return{
        "analysis": result
    }