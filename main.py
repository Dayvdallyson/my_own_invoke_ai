import os
import requests
from dotenv import load_dotenv

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
anthropic_api_url = "https://api.anthropic.com"
anthropic_api_url_messages_path = "/v1/messages"

user_name = input("Insert your name... \n")
prompt = f"Olá, meu nome é: {user_name}"

response = requests.post(
  f"{anthropic_api_url}{anthropic_api_url_messages_path}",
  headers={
    "x-api-key": anthropic_api_key,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
    },
  json={
    "max_tokens": 256,
    "messages": [
      {
        "content": prompt,
        "role": "user",
      }
    ],
    "model": "claude-haiku-4-5-20251001"
  }
  )

response_json = response.json()
assistant_message = response_json["content"][0]["text"]

print("Response", response_json)
print("Assistant message", assistant_message)
