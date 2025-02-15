from crewai import Agent

import os
from dotenv import load_dotenv

from tools import youtube_tool

# Load env vars
load_dotenv()

# Set OpenAI API Key and Model Name
os.environ["OPENAI_API_KEY"] = ""
model_name = "gpt-4-0125-preview"

# Create a blog content researcher
blog_researcher = Agent(
    role="YouTube Video Researcher",
    goal="Find relevant YouTube videos and extract key information for blog posts on the given topic.",
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in analyzing YouTube content related to AI, Data Science, Machine Learning, "
        "and Generative AI. You can quickly identify the most informative videos and extract the key points."
    ),
    tools=[youtube_tool],
    allow_delegation=False,
    llm=model_name  # Use the string model name
)

# Create a blog writer agent
blog_writer = Agent(
    role="Blog Writer",
    goal="Craft compelling and informative blog posts based on research findings.",
    verbose=True,
    memory=True,
    backstory=(
        "You have a talent for simplifying complex tech topics and creating engaging narratives. You turn "
        "research findings into accessible and captivating blog content."
    ),
    allow_delegation=False,
    llm=model_name,
    tools=[youtube_tool]
)
