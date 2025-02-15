import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

# Load env vars
load_dotenv()

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI LLM model
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# Invoke the model
response = llm.invoke("What is generative AI?")
print(response)
