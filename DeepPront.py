from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def prontCreator():
    x = input("Escribe tu consulta:")
    return x


client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),  
    base_url="https://openrouter.ai/api/v1"  
)


chat = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=
    ####
    [{
        "role": "user",
        "content": f"{prontCreator()}"   #Aqui va el contenido de la consulta
    }]
    

)


if chat.choices and chat.choices[0].message.content:
    print("Respuesta del modelo:", chat.choices[0].message.content)
else:
    print("La respuesta no contiene contenido o está vacía.")