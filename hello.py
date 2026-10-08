from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=300,
    system="You are a friendly customer support agent for an online sneaker store.",
    messages=[
        {"role": "user", "content": "Hi! Do you ship internationally?"}
    ],
)

print(response.content[0].text)
print(response.usage)
