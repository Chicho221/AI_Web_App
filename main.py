from fastapi import FastAPI
from analyzer import analyzer

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'AI Job Analyzer API is running'}