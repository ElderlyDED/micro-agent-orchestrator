from typing import List
from agent import BaseAgent
from memory import SharedMemory

class Orchestrator:
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents
        self.memory = SharedMemory()

    def run_pipeline(self, initial_input: str) -> str:
        current_input = initial_input
        self.memory.clear()

        for agent in self.agents:
            # We can optionally include previous context, but for simple sequential, 
            # we just pass the current input.
            prompt = f"Context from previous steps:\n{self.memory.get_full_history()}\n\nCurrent Task/Input:\n{current_input}"
            
            output = agent.run(prompt)
            self.memory.add_entry(agent.role, current_input, output)
            
            current_input = output
            
        return current_input
