import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
client = InferenceClient(token=HF_API_KEY)

def ask_huggingface(prompt: str, model="google/flan-t5-base") -> str:
    resp = client.text_generation(prompt, model=model, max_new_tokens=100, temperature=0.7)
    return resp.generated_text