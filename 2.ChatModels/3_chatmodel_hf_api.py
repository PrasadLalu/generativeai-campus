import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load env vars
load_dotenv()

# Set HuggingFace API Key
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

# Initialize the Hugging Face model
llm = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation"
    )
)

# Invoke the model and print response
response = llm.invoke("What is generative AI?")
print(response.content)
