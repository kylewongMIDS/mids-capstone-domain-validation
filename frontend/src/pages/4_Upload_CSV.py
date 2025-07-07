import streamlit as st
import pandas as pd
import requests
from app_utils import csv_to_lists, pred_to_csv

# sessions state info
selected_ca = st.session_state.get('selected_ca', 'Unknown CA')



# API Gateway info
url = "https://5edsvi6tk3.execute-api.us-east-1.amazonaws.com/default/FeatureExtractorContainer"
headers = {"Content-Type": "application/json"}




st.title("Step 3: 🐟 Phish Fence Manual Upload")
st.markdown("#### Predict malicious domains before provisioning certificates")
st.markdown("*By Kyle Wong, Clifton Harris, Andres Nieto*")
st.markdown("---")
st.markdown("### 📁 Upload a CSV of domains")


file_upload = st.file_uploader('Required columns: [san_identities, not_before, not_after]', type='csv')






# if file_upload:
#     with st.spinner("Processing file..."):
        
#         try:
#             clean_domain, not_before, not_after = csv_to_lists(file_upload)
#         except Exception as e:
#             st.error(f"Data loading error: {e}")
#             st.stop()

#         try:
#             payload = {
#                 'clean_domain': clean_domain,
#                 'not_before': not_before,
#                 'not_after': not_after
#             }
            
#             endpoint = 'http://127.0.0.1:8000/predict'
#             response = requests.post(endpoint, json=payload)
            
#             if response.status_code == 200:
#                 st.write(response.json())
            
#             #     # st.write('success')
#             # else:
#             #     st.write(response.status_code())
#         except Exception as e:
#             st.write('issue in place #1')
#             st.error(f"Preprocessing error: {e}")
#             st.stop()
        

# else:
#     st.info("📄 Please upload a CSV file to begin.")


if file_upload:
    with st.spinner("Processing file..."):
        
        
        try:
            payload = csv_to_lists(uploaded_file=file_upload, ca_name=selected_ca)
        except Exception as e:
            st.error(f'Issue with uploaded file. Please ensure the only columns are: san_identities, not_before, not_after')
        
        try:
            if st.button("Submit"):

                # response = requests.post(url, headers=headers, json=payload)
                
                # to delete, used for testing pred to csv function
                response = {
                    "features":
                        [
                            {
                                "parsed_domainname": "secure-login-paypal.net",
                                "prediction": 0.7142857143
                                },
                            {
                                "parsed_domainname": "secure-login-venmo.net",
                                "prediction": 0.8142857143
                                },
                            {
                                "parsed_domainname": "go0gle.com",
                                "prediction": 0.3428571429
                                },
                            {
                                "parsed_domainname": "facebo0k.com",
                                "prediction": 0.4
                                }
                            ]
                        }
                
                
                # if response.status_code == 200:
                if response:
                    st.success("✅ Successfully received predictions!")
                    # st.write(response)
                    # st.json(response.json())
                    csv_data = pred_to_csv(response)
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
            st.write(f'Exception message: {e}')

else:
    st.info("📄 Please upload a CSV file to begin.")

# Footer
st.markdown("---")
st.caption("© 2025 MIDS Capstone — UC Berkeley")