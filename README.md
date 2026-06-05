Markdown

# 🤖 Micro-Agent Orchestrator

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![AI Model](https://img.shields.io/badge/AI-GPT--4o-orange)

A lightweight, modular Python framework for designing and orchestrating AI agent pipelines. 

This system was built for those who love to assemble complex architectures, think through system design, and heavily automate multi-step processes. Instead of relying on monolithic LLM calls, **Micro-Agent Orchestrator** allows you to chain specialized AI agents together, passing shared context and memory seamlessly from one task to the next.

## ✨ Core Features

* **Sequential Orchestration:** Chain multiple agents (e.g., Analyst -> Critic -> Writer) to solve complex workflows sequentially.
* **Shared Memory Context:** Agents automatically pass outputs and preserve historical context without exceeding token limits.
* **GitHub Models Integration:** Natively built to work with `azure-ai-inference` and GitHub Models API (GPT-4o).
* **Fault Tolerance:** Built-in retry logic and context overflow protection.

## 🚀 Quick Start

### 1. Installation
Clone the repository and install the required dependencies:
```bash
git clone [https://github.com/ElderlyDED/micro-agent-orchestrator.git](https://github.com/ElderlyDED/micro-agent-orchestrator.git)
cd micro-agent-orchestrator
pip install -r requirements.txt

2. Environment Setup

Create a .env file in the root directory and add your GitHub token:
Ini, TOML

GITHUB_TOKEN=your_github_personal_access_token

3. Usage Example
Python

from agents.agent import BaseAgent
from core.orchestrator import Orchestrator

# Initialize specialized agents
analyst = BaseAgent(role="Analyst", prompt="Analyze the raw data and extract key metrics.")
writer = BaseAgent(role="Writer", prompt="Rewrite the metrics into a clear executive summary.")

# Build and run the pipeline
pipeline = Orchestrator(agents=[analyst, writer])
result = pipeline.run("Raw input data goes here...")

print(result)

🏗️ Architecture Design

The framework is highly modular, separating the API client layer, memory management, and agent logic. This makes it incredibly easy to scale the system, add custom parsing tools, or swap out the underlying LLM without rewriting the core orchestration logic.
