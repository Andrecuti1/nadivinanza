import streamlit as st
import random

# Lista de adivinanzas (pregunta y respuesta)
adivinanzas = [
    {"question": "¿Cuál es el animal más grande del mundo?", "answer": "ballena azul"},
    {"question": "¿Cuántos planetas tiene el sistema solar?", "answer": "8"},
    {"question": "¿En qué año llegó el hombre a la luna?", "answer": "1969"},
    {"question": "¿Cuál es la capital de Francia?", "answer": "parís"},
    {"question": "¿Cuántos continentes hay en el mundo?", "answer": "7"}
]

# Función para elegir una adivinanza aleatoria
def get_random_adivinanza():
    return random.choice(adivinanzas)

# Título de la aplicación
st.title("Juego de Adivinanzas")

# Elegir una adivinanza aleatoria
adivinanza_actual = get_random_adivinanza()

# Mostrar la adivinanza
st.subheader("Adivina la respuesta:")
st.write(adivinanza_actual["question"])

# Crear un contenedor con dos columnas: una para la respuesta y otra para el botón
col1, col2 = st.columns([3, 1])

# En la columna 1, colocar la caja de texto para la respuesta
respuesta_usuario = col1.text_input("Tu respuesta:")

# En la columna 2, colocar el botón para cambiar la adivinanza
if col2.button("Cambiar Adivinanza"):
    adivinanza_actual = get_random_adivinanza()
    st.experimental_rerun()

# Verificar si la respuesta es correcta
def verificar_respuesta(respuesta_usuario, respuesta_correcta):
    return respuesta_usuario.strip().lower() == respuesta_correcta.strip().lower()

# Al hacer clic en el botón de verificación
if st.button("Verificar"):
    if verificar_respuesta(respuesta_usuario, adivinanza_actual["answer"]):
        st.success("¡Correcto! 🎉")
        st.markdown(":star: :star: :star:")  # Mostrar estrellas
    else:
        st.error("¡Incorrecto! Intenta de nuevo.")
