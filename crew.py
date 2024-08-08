from crewai import Agent, Task, Crew, Process
from agents import product_manager, coder
from tasks import task1, task2

crew = Crew(
    agents=[product_manager, coder],
    tasks=[task1, task2],
    verbose=2,
)
result = crew.kickoff()
print("######################")
# print(result)