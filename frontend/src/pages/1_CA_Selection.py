import streamlit as st

st.set_page_config(page_title="CA Selection", layout="wide")
st.markdown("""
    <style>
    .gold-text {
        font-size: 48px;
        font-weight: bold;
        color: #d4af37;
    }
    </style>

    <div class="gold-text">PhishFence</div>
""", unsafe_allow_html=True)
st.subheader("Step 1: Select a Certificate Authority")

cas = [
    "Actalis", "Add Trust", "Certum", "Comodo", "DigiCert", "Entrust",
    "GeoTrust", "GlobalSign", "GoDaddy", "QuoVadis", "Sectigo", "SecureTrust", "Verisign"
]

selected_ca = st.selectbox("Please select your organization:", cas)

if st.button("Next"):
    st.session_state.selected_ca = selected_ca
    st.switch_page("pages/2_Choose_Input_Method.py")


# # Footer
# st.markdown("---")
# st.caption("© 2025 MIDS Capstone — UC Berkeley")