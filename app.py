#Load variables from .env
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

#Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

#Send request to the model
response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain artificial intelligence in one simple paragraph."
)

#Display the response
print(response.output_text)