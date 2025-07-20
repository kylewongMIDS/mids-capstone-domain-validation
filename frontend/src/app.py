import streamlit as st

st.set_page_config(page_title="Phish Fence", layout="wide")
st.title("🐟 Phishfence")
st.subheader('Our Mission')
st.write('''Empowering Certificate Authorities to protect internet trust by 
         proactively flagging suspicious domain requests before they become threats''')

if st.button("Let's get started"):
    st.switch_page("pages/1_CA_Selection.py")
    