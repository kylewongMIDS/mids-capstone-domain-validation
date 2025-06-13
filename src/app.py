import streamlit as st
from model import random_guess
from utils import csv_to_list, dict_to_csv

st.title("Domain Classifier")
st.subheader('MIDS Capstone Project')
st.write('Kyle Wong, Clifton Harris, Andres Nieto')

file_upload = st.file_uploader('Upload a single column of domains', type='csv')

if file_upload:
    domain_list = csv_to_list(file_upload)
    guesses = random_guess(domain_list)
    output_file = dict_to_csv(data=guesses)
    
    st.download_button('Download results', output_file, file_name = f'{file_upload.name}_predictions.csv')
    # st.write(guesses)
    
else:
    st.write("Please upload a csv of domains")
