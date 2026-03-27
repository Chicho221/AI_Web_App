from openai import OpenAI
from openai import RateLimitError
from config import API_KEY

client = OpenAI(api_key = API_KEY)

def analyzer(job):
    prompt = f"""
    Analyze this job:

    Title: {job['title']}
    Company: {job['company']}
    
    Respond in format:
    Summary:
    Skills:
    Level:
    """

    try:
        response = client.chat.completions.create(
        model="gpt-40-mini",
        messages = [
            {"role": "user", "content": prompt}
        ]
        )
        return response.choices[0].message.content
    except RateLimitError:
        print("Rate limit exceeded!")
        return