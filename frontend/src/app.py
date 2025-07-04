import streamlit as st
import pandas as pd
import requests
from app_utils import csv_to_lists

st.title(":fish Phish Fence")
st.markdown("#### Predict malicious domains before provisioning certificates")
st.markdown("*By Kyle Wong, Clifton Harris, Andres Nieto*")
st.markdown('API Documentation: [Click Here](http://127.0.0.1:8000/docs#/)')
st.markdown("---")


st.markdown("### 📁 Upload a CSV of domains")

file_upload = st.file_uploader('Match columns exactly: [clean_domain, not_before, not_after]', type='csv')

if file_upload:
    with st.spinner("Processing file..."):
        
        try:
            clean_domain, not_before, not_after = csv_to_lists(file_upload)
        except Exception as e:
            st.error(f"Data loading error: {e}")
            st.stop()

        try:
            payload = {
                'clean_domain': clean_domain,
                'not_before': not_before,
                'not_after': not_after
            }
            
            endpoint = 'http://127.0.0.1:8000/predict'
            response = requests.post(endpoint, json=payload)
            
            if response.status_code == 200:
                st.write(response.json())
            
            #     # st.write('success')
            # else:
            #     st.write(response.status_code())
        except Exception as e:
            st.write('issue in place #1')
            st.error(f"Preprocessing error: {e}")
            st.stop()
        

else:
    st.info("📄 Please upload a CSV file to begin.")

# Footer
st.markdown("---")
st.caption("© 2025 MIDS Capstone — UC Berkeley")