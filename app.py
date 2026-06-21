from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent

topic = input("Enter a research topic: ")

plan = planner_agent(topic)

research = researcher_agent(topic)

analysis = analyst_agent(topic, research)

report = writer_agent(topic, analysis)

print("\n===== FINAL RESEARCH REPORT =====\n")

print(report)