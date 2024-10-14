import streamlit as st
import random

# Función para generar un ejercicio de cinemática
def generar_ejercicio():
    # Datos aleatorios para el ejercicio
    v0 = random.randint(5, 20)  # Velocidad inicial en m/s
    t = random.randint(1, 10)   # Tiempo en segundos
    a = random.randint(1, 5)    # Aceleración en m/s²

    # Ecuación de cinemática: d = v0 * t + (1/2) * a * t²
    d = v0 * t + 0.5 * a * (t ** 2)
    
    return v0, a, t, d

# Configuración inicial de la página
st.title("Ejercicios de Cinemática")

# Generar un nuevo ejercicio
v0, a, t, d_correcto = generar_ejercicio()

# Mostrar el ejercicio al usuario
st.write(f"Un objeto se mueve con una velocidad inicial de **{v0} m/s** y una aceleración de **{a} m/s²** durante **{t} segundos**.")
st.write("¿Cuál es la distancia recorrida por el objeto? (redondea tu respuesta a dos decimales)")

# Entrada del usuario para la respuesta
respuesta_usuario = st.number_input("Introduce tu respuesta:", format="%.2f")

# Botón para verificar la respuesta
if st.button("Verificar respuesta"):
    if respuesta_usuario == d_correcto:
        st.success("¡Correcto! La distancia recorrida es de {:.2f} metros.".format(d_correcto))
    else:
        st.error("Incorrecto. La distancia correcta es de {:.2f} metros.".format(d_correcto))


