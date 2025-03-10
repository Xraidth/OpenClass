from openai import OpenAI
from dotenv import load_dotenv
import os

def MyDeepClass():

    load_dotenv()

    def prontCreator():
        x = input("Tema del que hablaremos hoy:")

        r=f"""Escribe un texto como si fueras un profesor
            estructurado sobre {x} con el siguiente formato:
            - Inicia con un título claro, sin caracteres especiales como asteriscos o guiones.
            - Introduce el tema con una oración de bienvenida.
            - Explica los eventos en orden cronológico, mencionando fechas clave y personajes importantes.
            - Mantén párrafos concisos y enfocados en cada tema, período o concepto.
            - Usa un tono formal pero accesible, similar a una clase.
            - No incluyas caracteres especiales como * o _ para resaltar texto.
            - La respuesta debe tener un máximo de 7.500 tokens para asegurar que no se exceda el límite del modelo.
            - Finaliza sin preguntas ni nada, solo el texto que debes escribir."""


        return r


    client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),  
        base_url="https://openrouter.ai/api/v1"  
    )


    chat = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=
        
        [{
            "role": "user",
            "content": f"""{prontCreator()}"""   #Aqui va el contenido de la consulta     
        }]
        

    )

    r=""
    if chat.choices and chat.choices[0].message.content:
        r = chat.choices[0].message.content.replace('*', '')
        print("Respuesta del modelo:", r)

    else:
        print("La respuesta no contiene contenido o está vacía.")
    return r



