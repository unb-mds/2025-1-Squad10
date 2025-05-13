import streamlit as st

def login_page():
    st.title("Login")
    st.text_input("Usuário")
    st.text_input("Senha", type="password")
    st.button("Entrar")