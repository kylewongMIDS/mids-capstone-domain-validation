import streamlit as st

st.set_page_config(page_title="Phish Fence", layout="wide")
st.title("🐟 Phish Fence")
st.write('Welcome to Phish Fence, ')

if st.button("Let's get started"):
    st.switch_page(r"pages\1_CA_Selection.py")
    