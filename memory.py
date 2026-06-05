from typing import List, Dict, Any

class SharedMemory:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    def add_entry(self, agent_role: str, input_data: str, output_data: str):
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
        return history_str

    def get_last_output(self) -> str:
        if not self.history:
            return ""
        return self.history[-1]["output"]
    
    def clear(self):
        self.history = []
