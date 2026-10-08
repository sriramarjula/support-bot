from dotenv import load_dotenv
import anthropic

# Load the API key from .env and create the client
load_dotenv()
client = anthropic.Anthropic()

# The bot's personality and rules
# The bot's personality and rules
SYSTEM_PROMPT = """You are a customer support agent for an online sneaker store.

Rules:
- Keep answers short: 2-4 sentences.
- Plain text only. No markdown, headers, or bullet points.
- Do NOT invent products, prices, or policies. If you don't know,
  say you'll check with the team.
- Be friendly, but get to the point."""

# The conversation history (this is the bot's "memory")
messages = []

print("Support bot ready! Type 'quit' to exit.\n")

while True:
    # Ask the user for input
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Bye! 👋")
        break

    # 1. Add the user's message to the history
    messages.append({"role": "user", "content": user_input})

    # 2. Send the WHOLE history to Claude
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=300,
        system=SYSTEM_PROMPT,
        messages=messages,
    )

    # 3. Get the reply text and show it
    reply = response.content[0].text
    print("Bot:", reply)

    # 4. Add Claude's reply to the history (this is what makes it "remember")
    messages.append({"role": "assistant", "content": reply})

    # Bonus: watch the cost grow as the conversation gets longer
    print(f"   [tokens in: {response.usage.input_tokens}, out: {response.usage.output_tokens}]\n")