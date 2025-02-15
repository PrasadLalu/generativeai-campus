import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load env vars
load_dotenv()

# Set Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize qwen chat model
llm = ChatGroq(model="qwen-2.5-32b", groq_api_key=GROQ_API_KEY)

# Invoke the model
response = llm.invoke("What is generative AI?")
print(response.content)
