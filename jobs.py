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
    response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code

    data = response.json()
    
    if 'jobs' in data:
        for job in data['jobs']:
            st.write(job['title'], job['company'], job['location'])
    else:
        st.write("No jobs found.")

except requests.exceptions.RequestException as e:
    st.write(f"An error occurred: {e}")
