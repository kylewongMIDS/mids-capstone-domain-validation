import streamlit as st

st.title("Step 1: Select a Certificate Authority")

cas = [
    "Actalis", "Add Trust", "Certum", "Comodo", "DigiCert", "Entrust",
    "GeoTrust", "GlobalSign", "GoDaddy", "QuoVadis", "Sectigo", "SecureTrust", "Verisign"
]

selected_ca = st.selectbox("Choose a CA to begin:", cas)

if st.button("Next"):
    st.session_state.selected_ca = selected_ca
    st.switch_page("pages/2_Choose_Input_Method.py")