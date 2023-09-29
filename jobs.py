import streamlit as st
import requests 

st.title('Job Search')

companies = st.multiselect('Select Companies', ['Google', 'Facebook', 'Microsoft'])

API_KEY = 'AIzaSyAuFskRWKMFZailNaCf02sAfnbqz9IP3JE'  # Consider moving this to a secure location

url = 'https://jobs.googleapis.com/v2/jobs/search' 

if companies:
  params = {
    'q': 'python developer', 
    'companyNames': ','.join(companies),  
    'location': 'San Francisco, CA',
    'key': API_KEY
  }
else:
  params = {
    'q': 'python developer',  
    'location': 'San Francisco, CA',
    'key': API_KEY
  }
  
try:
    response = requests.get(url, params=params)
    response.raise_for
