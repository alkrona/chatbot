import os 
import streamlit as st
import pandas as pd
import requests
from call_api import send_api_request
st.write("# Chat with Property_data Data ")
df = pd.read_csv("data/property_data.csv")
with st.expander(" Dataframe Preview"):
    st.write(df.head(10))
query = st.text_area("Chat with Dataframe")
st.write(query)
if query:
    response = send_api_request(query)
    if isinstance(response, bytes):
        response = response.decode('utf-8') 
    st.markdown(response) 