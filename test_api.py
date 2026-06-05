import os
import pytest
from agent import BaseAgent

def test_missing_token_raises_error():
    original_token = os.environ.get("GITHUB_TOKEN")
    if "GITHUB_TOKEN" in os.environ:
        del os.environ["GITHUB_TOKEN"]
        
    with pytest.raises(ValueError, match="GITHUB_TOKEN environment variable is missing"):
        BaseAgent(role="Test", system_prompt="Test")
        
    if original_token is not None:
        os.environ["GITHUB_TOKEN"] = original_token

def test_agent_initialization():
    os.environ["GITHUB_TOKEN"] = "dummy_token"
    agent = BaseAgent(role="Tester", system_prompt="You are a tester.")
    assert agent.role == "Tester"
    assert agent.model == "openai/gpt-4o"
