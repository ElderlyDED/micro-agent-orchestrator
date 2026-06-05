from agent import BaseAgent
from orchestrator import Orchestrator

def run_example():
    analyst = BaseAgent(
        role="Analyst",
        system_prompt="You are an Analyst. Your job is to break down the given task, extract key points, and propose a preliminary analytical solution. Be highly detailed and analytical."
    )
    
    critic = BaseAgent(
        role="Critic",
        system_prompt="You are a Critic. Your job is to review the Analyst's solution. Find flaws, missing perspectives, or logical inconsistencies. Provide constructive criticism and suggest improvements."
    )
    
    writer = BaseAgent(
        role="Writer",
        system_prompt="You are a Writer. Your job is to take the original task, the Analyst's initial solution, and the Critic's review, and synthesize them into a clear, engaging, and final comprehensive answer. Format your response nicely using Markdown."
    )

    orchestrator = Orchestrator(agents=[analyst, critic, writer])
    
    task = "Explain the potential impact of quantum computing on modern cryptography."
    print(f"Initial Task: {task}\n")
    print("Running pipeline...\n")
    
    final_output = orchestrator.run_pipeline(task)
    
    print("=== Pipeline Complete ===")
    print("\n--- Final Output ---")
    print(final_output)
    
    print("\n--- Context History ---")
    print(orchestrator.memory.get_full_history())

if __name__ == "__main__":
    run_example()
