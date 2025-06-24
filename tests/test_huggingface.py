# tests/test_huggingface.py

import pytest
from unittest.mock import MagicMock, patch
from src.llm_clients import hf_client

@pytest.fixture(autouse=True)
def mock_hf_client(monkeypatch):
    fake_resp = MagicMock()
    fake_resp.generated_text = "La capital de Francia es París."
    fake_client = MagicMock()
    fake_client.text_generation.return_value = fake_resp
    monkeypatch.setattr(hf_client, "client", fake_client)

def test_hf_response():
    resp = hf_client.ask_huggingface("¿Cuál es la capital de Francia?")
    assert "París" in resp or "Paris" in resp
