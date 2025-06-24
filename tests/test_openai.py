import pytest
from src.llm_clients.openai_client import ask_openai

def test_openai_response():
    prompt = "¿Cuál es la capital de Francia?"
    response = ask_openai(prompt)
    assert "París" in response or "Paris" in response