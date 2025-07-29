import streamlit as st
import time

st.set_page_config(page_title="Phish Fence", layout="wide")

st.markdown("""
    <style>
    .gold-text {
        font-size: 48px;
        font-weight: bold;
        color: #d4af37;
    }
    </style>

    <div class="gold-text">PhishFence</div>
    <p style="color: #c0c0c0; font-size: 1.5rem; font-weight: 300;">
        Protecting <b style='color:#d4af37;'>TRUST</b> one <b style='color:#d4af37;'>DOMAIN</b> at a time.
    </p>
""", unsafe_allow_html=True)


if st.button("Let's get started"):
    st.switch_page("pages/1_CA_Selection.py")
