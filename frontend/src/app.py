import streamlit as st
import pandas as pd
# from model.model import random_guess
from model.model_utils import preprocess_domains, load_model
# from utils import csv_to_list, dict_to_csv
# from aws_clients import write_csv_to_s3, retrieve_csv_from_s3, batch_transformation_job

st.title("🔍 Domain Classifier")
st.markdown("#### MIDS Capstone Project")
st.markdown("*By Kyle Wong, Clifton Harris, Andres Nieto*")
st.markdown("---")


st.markdown("### 📁 Upload Your Domain CSV")
file_upload = st.file_uploader('Upload a CSV file containing a single column of domains', type='csv')

if file_upload:
    with st.spinner("Processing file..."):
        
        # Read uploaded file
        try:
            df_raw = pd.read_csv(file_upload)
        except Exception as e:
            st.error(f"Data loading error: {e}")
            st.stop()
        
        # Preprocess domains using your function
        try:
            df_preprocessed = preprocess_domains(df_raw)
        except Exception as e:
            st.error(f"Preprocessing error: {e}")
            st.stop()
        
        # Load model
        model = load_model()
        
        # Make predictions
        try:
            predictions = model.predict(df_preprocessed)
            df_raw['prediction'] = predictions
        except Exception as e:
            st.error(f"Prediction error: {e}")
            st.stop()
            
        # Show and download results
        st.dataframe(df_raw[['not_before','not_after','clean_domain','blacklist_flag','prediction']])
        
        
        # try:
        #     # domain_list = csv_to_list(file_upload)

        #     # # Upload input file to S3
        #     # input_file_id = write_csv_to_s3(file_upload)
        #     # st.success(f"✅ Domain file uploaded to S3: `{input_file_id}`")

        #     # # run batch transformation job
        #     # batch_transformation_job(model_name = 'random_forest_model_v1', input_file_id = input_file_id)            
        #     # st.success(f"✅ Domain predictions finished")
            
        #     # # retrieve predictions from s3
        #     # output_file = retrieve_csv_from_s3(input_file_id)
        #     # st.success(f"✅ Prediction file retrieved from s3")

        #     # # Run prediction
        #     # # guesses = random_guess(domain_list)

        #     # # Convert results to CSV
        #     # # output_file = dict_to_csv(data=guesses)

        #     # # Download button
        #     # st.markdown("### 📥 Download Predictions")
        #     # st.download_button(
        #     #     label="Download CSV",
        #     #     data=output_file,
        #     #     file_name=f"{file_upload.name}_predictions.csv",
        #     #     mime="text/csv",
        #     # )
        
        # except Exception as e:
        #     st.error(f"🚨 An error occurred: {e}")
else:
    st.info("📄 Please upload a CSV file to begin.")

# Footer
st.markdown("---")
st.caption("© 2025 MIDS Capstone — UC Berkeley")