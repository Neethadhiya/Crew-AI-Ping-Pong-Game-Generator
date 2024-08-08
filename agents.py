from crewai import Agent, Task, Crew
# You need to build and extend your own agent logic with the CrewAI BaseAgent class then import it here.
from langchain_openai import OpenAI
import os
from langchain_community.agent_toolkits.load_tools import load_tools
from dotenv import load_dotenv
load_dotenv()
llm = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    model_name=os.environ["OPENAI_MODEL_NAME"]
)
langchain_tools = load_tools(["google-serper"], llm=llm)
class CodeSavingAgent(Agent):
    def handle_task(self, task):
        try:
            # Generate code based on the task description
            code = super().handle_task(task)
            print("==================================")
            print(f"Generated code: {code}")  # Debug print
            print("=======================================")
            # Use a fixed filename
            file_name = "ping_pong_game.py"
            print(f"Saving code to file: {file_name}")  # Debug print
            
            # Save the code to the specified Python file
            with open(file_name, "w") as file:
                file.write(code)
            
            print(f"Code successfully written to {file_name}")
            return code
        except Exception as e:
            print(f"An error occurred while handling the task: {e}")
            return None
product_manager = Agent(
    role='Product Manager',
    goal='Define requirements for a software product',
    backstory="You are an experienced Product Manager skilled in defining clear and concise requirements.",
    verbose=True,
    # tools = [tool1, tool2]
)

coder = CodeSavingAgent(
    role='Software Developer',
    goal='Develop software based on the provided requirements',
    backstory="You are a skilled software developer proficient in coding robust and efficient applications.",
    verbose=True,
)
