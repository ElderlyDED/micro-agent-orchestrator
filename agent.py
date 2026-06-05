import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

class BaseAgent:
    def __init__(self, role: str, system_prompt: str, model: str = "openai/gpt-4o"):
        self.role = role
        self.system_prompt = system_prompt
        self.model = model
        
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            # We'll handle this properly in step 8, for now just a simple check or allow it to fail
            pass
            
        endpoint = "https://models.github.ai/inference"
        self.client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token) if token else AzureKeyCredential("dummy")
        )

    def run(self, input_text: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            UserMessage(content=input_text)
        ]
        
        response = self.client.complete(
            messages=messages,
            model=self.model,
            max_tokens=2048,
        )
        return response.choices[0].message.content
