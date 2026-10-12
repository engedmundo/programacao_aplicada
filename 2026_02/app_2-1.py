import streamlit as st

st.title("Calculadora de dureza Rockwell")
st.write("Calcula a média de dureza a partir de 3 medições informadas")

# Criar 3 colunas
col1, col2, col3 = st.columns(3)

# Para inserir valores em cada coluna
with col1:
    medicao_1 = st.number_input("Medição 01 (HRC)")

with col2:
    medicao_2 = st.number_input("Medição 02 (HRC)")

with col3:
    medicao_3 = st.number_input("Medição 03 (HRC)")

botao = st.button("Calcular Média")

if botao == True:
    media = (medicao_1 + medicao_2 + medicao_3) / 3
    st.metric("Dureza média", f"{media:.2f} HRC")
