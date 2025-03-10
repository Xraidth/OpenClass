from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def prontCreator():
    return input("Tú: ")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("La API key no se encontró en el archivo .env")

client = OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")

# Inicializa el historial de mensajes
messages = []

while True:
    user_input = prontCreator()
    
    # Agrega el mensaje del usuario al historial
    messages.append({"role": "user", "content": user_input})

    # Obtén la respuesta del modelo
    chat = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=messages
    )

    # Muestra la respuesta
    response = chat.choices[0].message.content
    print("Bot:", response)

    # Agrega la respuesta del modelo al historial
    messages.append({"role": "assistant", "content": response})



