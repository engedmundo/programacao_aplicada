import streamlit as st     # Necessário para utlizar a biblioteca streamlit

st.title("Cálculo de tensão")

forca = st.number_input("Força (N)")
area = st.number_input("Área (mm2)")

calcular = st.button("Calcular")

if calcular is True:
    sigma = forca / area
    st.metric("Tensão:", f"{sigma} MPa")
    st.write(f"Tensão: {sigma} MPa")