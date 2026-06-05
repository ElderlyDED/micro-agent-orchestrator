import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from tenacity import retry, stop_after_attempt, wait_exponential
from logger import get_logger

logger = get_logger(__name__)

class BaseAgent:
    def __init__(self, role: str, system_prompt: str, model: str = "openai/gpt-4o"):
        self.role = role
        self.system_prompt = system_prompt
        self.model = model
        
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            logger.error("GITHUB_TOKEN is missing.")
            raise ValueError("GITHUB_TOKEN environment variable is missing. Please set it to use the GitHub Models API.")
            
        endpoint = "https://models.github.ai/inference"
        self.client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token)
        )

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def _call_api(self, messages):
        logger.info(f"Agent '{self.role}' is calling the API...")
        return self.client.complete(
            messages=messages,
            model=self.model,
            max_tokens=2048,
        )

    def run(self, input_text: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            UserMessage(content=input_text)
        ]
        
        try:
            response = self._call_api(messages)
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Agent '{self.role}' API call failed: {e}")
            raise
