# src/llm_clients/claude_client.py

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask_claude(prompt: str, model="claude-opus-4-0", temperature=0.7) -> str:
    resp = client.messages.create(
        model=model,
        max_tokens=300,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}]
    )
    #Unir los textos de los bloques de respuesta
    return "".join(block.text for block in resp.content)
