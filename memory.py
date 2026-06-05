from typing import List, Dict, Any
from logger import get_logger

logger = get_logger(__name__)

class SharedMemory:
    def __init__(self, max_history_length: int = 4000):
        self.history: List[Dict[str, Any]] = []
        self.max_history_length = max_history_length

    def add_entry(self, agent_role: str, input_data: str, output_data: str):
        logger.info(f"Adding memory entry for {agent_role}")
        self.history.append({
            "agent_role": agent_role,
            "input": input_data,
            "output": output_data
        })

    def get_full_history(self) -> str:
        if not self.history:
            return "No history available."
        
        history_str = "--- Context History ---\n"
        for i, entry in enumerate(self.history):
            history_str += f"[{i+1}] {entry['agent_role']}:\n"
            history_str += f"Input: {entry['input']}\n"
            history_str += f"Output: {entry['output']}\n"
            history_str += "-" * 20 + "\n"
        
        if len(history_str) > self.max_history_length:
            logger.warning(f"Context truncated from {len(history_str)} to {self.max_history_length} chars.")
            history_str = history_str[-self.max_history_length:]
            
        return history_str

    def get_last_output(self) -> str:
        if not self.history:
            return ""
        return self.history[-1]["output"]
    
    def clear(self):
        logger.info("Clearing shared memory.")
        self.history = []

