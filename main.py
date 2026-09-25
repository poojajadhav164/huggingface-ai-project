import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"]
)

print("=================================")
print("       🤖 AI CHATBOT")
print("=================================")
print("Type your question below.")
print("Type 'exit' to close the chatbot.")
print("=================================")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("AI: Goodbye! 👋")
        break

    if question.strip() == "":
        print("AI: Please enter a question.")
        continue

    try:
        response = client.chat.completions.create(
            model="Qwen/Qwen3.8-Flash-Next:featherless-ai",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content
        print("\nAI:", answer)

    except Exception as e:
        print("\nError:", e)
        
