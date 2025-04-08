import os
from dotenv import load_dotenv
from openai import OpenAI
from app.utils import getenv

def query_llm(prompt: str) -> str:
    """
    Send a prompt to an LLM and get the response.
    
    In a real implementation, this would call OpenAI's API or another LLM provider.
    For now, we return a mock response.
    """
    try:
        
        client = OpenAI(api_key=getenv("OPENAI_API_KEY"))
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for internal company use."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling LLM API: {str(e)}"