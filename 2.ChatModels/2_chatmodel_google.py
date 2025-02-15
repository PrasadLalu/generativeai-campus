import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load env vars
load_dotenv()

# Set Google API Key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini chat model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Invoke the model
response = llm.invoke("What is generative AI?")
print(response.content)
