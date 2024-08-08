from crewai import Task
from agents import product_manager, coder

task1 = Task(
    description="Define the key requirements and features for a classic ping pong game. Be specific and concise.",
    expected_output="A clear and concise list of requirements for the ping pong game",
    agent=product_manager
)

task2 = Task(
    description="Based on the provided requirements, develop the code for the classic ping pong game. Focus on gameplay mechanics and a simple user interface.",
    expected_output="Complete code for the ping pong game.The code should be saved in file ping_pong_game.py",
    agent=coder
)