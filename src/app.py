import streamlit as st

st.title("Hello from Poetry + Streamlit in Docker!")

user_input = st.text_input("Enter some text:")

if user_input:
    st.write(f"You typed: {user_input}")
else:
    st.write("Please type something above.")
