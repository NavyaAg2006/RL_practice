from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv(override=True)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Key loaded:", bool(os.getenv("GROQ_API_KEY")))

for model in client.models.list().data:
    print(model.id)