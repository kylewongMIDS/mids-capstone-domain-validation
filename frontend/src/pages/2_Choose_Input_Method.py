import streamlit as st

st.set_page_config(page_title="Choose Input Method", layout="wide")
st.title("🐟 Phishfence")
st.subheader(f"Step 2: Choose Input Method")
st.write(f"You selected **{st.session_state.get('selected_ca', 'Unknown CA')}**")

option = st.radio("How would you like to submit domains?", ("Phishfence API", "Upload a CSV"))

if st.button("Continue"):
    if option == "Phishfence API":
        st.switch_page("pages/3_API_Instructions.py")
    else:
        st.switch_page("pages/4_Upload_CSV.py")


# Footer
st.markdown("---")
st.caption("© 2025 MIDS Capstone — UC Berkeley")