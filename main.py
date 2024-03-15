import openai

with open('secert.txt')as file:
    openai.api_key = file.read()


def get_api_response(prompt: str) -> str | None:
    text: str

def ask_gpt3.5(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.7,
      max_tokens=150
    )
    return response.choices[0].text.strip()

print("Welcome to Jarvis ChatBot!")
print("You can start talking with me. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Jarvis: Goodbye!")
        break
    response = ask_gpt3.5(user_input)
    print("Jarvis:", response)