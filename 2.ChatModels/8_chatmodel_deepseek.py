import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load env vars
load_dotenv()

# Set Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize deepseek chat model
llm = ChatGroq(model="deepseek-r1-distill-llama-70b", groq_api_key=GROQ_API_KEY)

# Invoke the model
response = llm.invoke("What is generative AI?")
print(response.content)
