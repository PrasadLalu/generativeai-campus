import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load env vars
load_dotenv()

# Set Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize mixtral chat model
llm = ChatGroq(model="mixtral-8x7b-32768", groq_api_key=GROQ_API_KEY)

# Invoke the model
response = llm.invoke("What is generative AI?")
print(response.content)
