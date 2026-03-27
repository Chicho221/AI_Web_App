from fastapi import FastAPI
from analyzer import analyze_job
from analyzer import analyze_jobFake

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'AI Job Analyzer API is running'}

# Analyze using predefined data
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