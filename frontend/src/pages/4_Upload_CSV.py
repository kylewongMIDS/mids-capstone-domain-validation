import streamlit as st
import requests
from app_utils import csv_to_lists
import json

# sessions state info
selected_ca = st.session_state.get('selected_ca', 'Unknown CA')


# API Gateway info
url = st.secrets["api"]["gateway_url"]
headers = {"Content-Type": "application/json"}

st.set_page_config(page_title="Upload CSV", layout="wide")
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
st.subheader("Step 3: Upload CSV")
st.markdown("Predict malicious domains before provisioning certificates")

with st.expander('Click to view the expected CSV format'):
    st.markdown("""
                | san_identities | not_before | not_after | domain_created |
                | --- | --- | --- | --- |
                | googlevads-cn.com, .ficoanalyticcloud.com, .dms.apset2.ficoanalyticcloud.com | 2024-06-01T00:00:00Z | 2024-09-01T00:00:00Z | 2021-04-19 21:44:18.000, null, 2023-04-13 09:25:58.000 |
                | go0gle.com, facebo0k.com | 2024-06-03T00:00:00Z | 2024-07-03T00:00:00Z | 2025-02-13 12:31:38.000, 2025-05-23 11:55:32.000 |
                | ... | ... | ... | ... |
                """)


file_upload = st.file_uploader(' ', type='csv')

if file_upload:
    with st.spinner("Processing file..."):
        
        
        try:
            payload = csv_to_lists(uploaded_file=file_upload, ca_name=selected_ca)
            payload_formatted = json.dumps(payload, indent=2)
            # st.write(payload_formatted)
        except Exception as e:
            st.error(f'Issue with uploaded file. Please ensure the only columns are: san_identities, not_before, not_after')
        
        try:
            if st.button("Submit"):

                response = requests.post(url, headers=headers, data=payload_formatted)
               
                if response.status_code == 200:
                    st.success("✅ Successfully received predictions!")
                    st.session_state.prediction_json = response.json()
                    st.session_state.file_name = file_upload.name
                    
                    # csv_data = pred_to_csv(response.json())
                    
                    # st.download_button(
                    #     label = 'Download Results',
                    #     data = csv_data,
                    #     file_name = f'PREDICTIONS_{file_upload.name}.csv',
                    #     mime='text/csv'
                    # )
                    st.switch_page("pages/5_Results.py")
                    
                else:
                    st.error(f"❌ Failed with status code {response.status_code}")
                    st.text(response.text)
        except Exception as e:
            st.write(response.text)
            st.write(f'Exception message: {e}')

# else:
    # st.info("📄 Please upload a CSV file to begin.")

# # Footer
# st.markdown("---")
# st.caption("© 2025 MIDS Capstone — UC Berkeley")