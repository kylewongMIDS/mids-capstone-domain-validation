import streamlit as st

st.title(f"Step 2: Choose Input Method")
st.write(f"You selected **{st.session_state.get('selected_ca', 'Unknown CA')}**")

option = st.radio("How would you like to submit domains?", ("Use API", "Upload CSV manually"))

if st.button("Continue"):
    if option == "Use API":
        st.switch_page("pages/3_API_Instructions.py")
    else:
        st.switch_page("pages/4_Upload_CSV.py")