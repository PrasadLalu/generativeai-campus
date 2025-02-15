from crewai import Task
from tools import youtube_tool
from agents import blog_researcher, blog_writer

# Create research task
research_task = Task(
    description=(
        "Research YouTube videos on the topic '{topic}'. Identify 2-3 of the most relevant videos that provide"
        "a comprehensive overview. Extract the key insights, arguments, and data points from these videos."
    ),
    expected_output="A detailed report summarizing the key findings from the selected YouTube videos. "
                    "Include video titles, channel names, and concise summaries of the content. "
                    "Focus on extracting information useful for creating a blog post.",
    tools=[youtube_tool],
    agent=blog_researcher
)

# Create write task
write_task = Task(
    description=(
        "Using the research report provided, write a compelling blog post on the topic '{topic}'. "
        "Ensure the blog post is informative, engaging, and easy to understand for a general audience."
        "Incorporate the key findings from the videos into the blog post seamlessly."
    ),
    expected_output="A well-written blog post (approximately 500-700 words) that summarizes the key concepts and "
                    "information from the YouTube videos. The blog post should be ready for publication.",
    agent=blog_writer,
    async_execution=False
)
