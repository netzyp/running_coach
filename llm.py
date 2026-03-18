from google import genai
from dotenv import load_dotenv



load_dotenv()

def coach_llm(data):
    client = genai.Client()
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", contents = data)
    return response.text
