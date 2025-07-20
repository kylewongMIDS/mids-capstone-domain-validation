import streamlit as st
import requests
from app_utils import csv_to_lists, pred_to_csv
import json

# sessions state info
selected_ca = st.session_state.get('selected_ca', 'Unknown CA')


# API Gateway info
url = st.secrets["api"]["gateway_url"]
headers = {"Content-Type": "application/json"}

st.set_page_config(page_title="Upload CSV", layout="wide")
st.title("🐟 Phishfence")
st.subheader("Step 3: Upload CSV")
st.markdown("Predict malicious domains before provisioning certificates")

with st.expander('Click to view the expected CSV format'):
    st.markdown("""
                | san_identities | not_before | not_after |
                | --- | --- | --- |
                | secure-login-paypal.net, secure-login-venmo.net | 2024-06-01T00:00:00Z | 2024-09-01T00:00:00Z |
                | go0gle.com, facebo0k.com | 2024-06-03T00:00:00Z | 2024-07-03T00:00:00Z |
                | google.com, facebook.com | 2024-06-04T00:00:00Z | 2024-08-04T00:00:00Z |
                """)


file_upload = st.file_uploader(' ', type='csv')

if file_upload:
    with st.spinner("Processing file..."):
        
        
        try:
            payload = csv_to_lists(uploaded_file=file_upload, ca_name=selected_ca)
            payload_formatted = json.dumps(payload, indent=2)
        except Exception as e:
            st.error(f'Issue with uploaded file. Please ensure the only columns are: san_identities, not_before, not_after')
        
        try:
            if st.button("Submit"):

                response = requests.post(url, headers=headers, data=payload_formatted)
               
                if response.status_code == 200:
                    st.success("✅ Successfully received predictions!")
                    csv_data = pred_to_csv(response.json())
                    st.download_button(
                        label = 'Download Results',
                        data = csv_data,
                        file_name = f'PREDICTIONS_{file_upload.name}.csv',
                        mime='text/csv'
                    )
                else:
                    st.error(f"❌ Failed with status code {response.status_code}")
                    st.text(response.text)
        except Exception as e:
            st.write(response.text)
            st.write(f'Exception message: {e}')

# else:
    # st.info("📄 Please upload a CSV file to begin.")

# Footer
st.markdown("---")
st.caption("© 2025 MIDS Capstone — UC Berkeley")