import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
INPUT = os.getenv("INPUT_DIRECTORY")
OUTPUT = os.getenv("OUTPUT_DIRECTORY")

messages = [
    {"role": "system", "content": "Ты переписываешь тексты своими словами сохраняя смысл"}
]

count_files = len(os.listdir(INPUT))
complete = 0

for file_name in os.listdir(INPUT):
    with open(os.path.join(INPUT, file_name), 'r') as file:
        text = file.read()
        file.close()

    messages.append({"role": "user", "content": text})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion.choices[0].message.content

    with open(os.path.join(OUTPUT, file_name), 'w') as file:
        file.write(chat_response)
        file.close()

    complete += 1
    print(f"Progress: {complete} / {count_files}")
