from crewai import Process, Crew
from tasks import research_task, write_task
from agents import blog_researcher, blog_writer


crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Start the execution process
result = crew.kickoff(inputs={"topic": "All You Need To Know About DeepSeek- ChatGPT Killer"})
print(result)
