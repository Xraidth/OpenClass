import pyttsx3
import DeepClass as dc

def leer_texto(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Ajusta la velocidad de la voz
    engine.setProperty('volume', 1)  # Ajusta el volumen (de 0 a 1)
    engine.say(texto)
    engine.runAndWait()

# Ejemplo de uso
texto = dc.MyDeepClass()
leer_texto(texto)
