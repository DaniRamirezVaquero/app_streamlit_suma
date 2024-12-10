import streamlit as st

st.title('Aplicación suma streamlit')
# Input fields for the two numbers
num1 = st.number_input('Ingrese el primer número', value=0)
num2 = st.number_input('Ingrese el segundo número', value=0)

# Button to perform the addition
if st.button('Sumar'):
  resultado = num1 + num2
  st.success(f'{num1} + {num2} = {resultado}')
