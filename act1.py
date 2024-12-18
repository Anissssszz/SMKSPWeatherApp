import streamlit as st

st.title("My First Dashboard App")
st.write("Hello, welcome to my first Dashoard app!")

user_input = st.text_input("Enter your name:")

st.write(f"Congratulations, {user_input!} this is your first dashboard")