import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if API key exists
if not GOOGLE_API_KEY:
    raise ValueError("Google API Key not found! Please set it in the .env file.")

# Initialize the Generative AI client
genai.configure(api_key=GOOGLE_API_KEY)

# List available models
try:
    available_models = genai.list_models()
    print("Available models:")
    for model in available_models:
        print(f"- {model['name']}: {model['description']}")
except Exception as e:
    print(f"Error: {e}")
