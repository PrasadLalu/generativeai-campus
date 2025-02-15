import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load env vars
load_dotenv()

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI chat model
llm = ChatOpenAI(model="gpt-4o")

# Invoke the model
response = llm.invoke("What is generative AI?")
print(response.content)
