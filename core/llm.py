from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

llm = genai.Client(
    api_key = os.environ["GOOGLE_API_KEY"]
)