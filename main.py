import argparse
from agent import BaseAgent
from orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description="Micro-Agent Orchestrator CLI")
    parser.add_argument("--task", type=str, required=True, help="The task for the agent pipeline to execute")
    args = parser.parse_args()

    analyst = BaseAgent(
        role="Analyst",
        system_prompt="You are an Analyst. Break down the given task, extract key points, and propose a preliminary analytical solution. Be highly detailed and analytical."
    )
    
    critic = BaseAgent(
        role="Critic",
        system_prompt="You are a Critic. Review the Analyst's solution. Find flaws, missing perspectives, or logical inconsistencies. Provide constructive criticism and suggest improvements."
    )
    
    writer = BaseAgent(
        role="Writer",
        system_prompt="You are a Writer. Take the original task, the Analyst's initial solution, and the Critic's review, and synthesize them into a clear, engaging, and final comprehensive answer. Format your response nicely using Markdown."
    )

    orchestrator = Orchestrator(agents=[analyst, critic, writer])
    
    print(f"Task: {args.task}\n")
    print("Running pipeline...")
    
    final_output = orchestrator.run_pipeline(args.task)
    
    print("\n" + "="*40)
    print("FINAL OUTPUT")
    print("="*40)
    print(final_output)

if __name__ == "__main__":
    main()
