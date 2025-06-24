# tests/test_claude.py

from src.llm_clients.claude_client import ask_claude

def test_claude_response():
    prompt = "¿Cuál es la capital de Francia?"
    response = ask_claude(prompt)
    assert "París" in response or "Paris" in response
