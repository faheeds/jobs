import streamlit as st
import requests 
from oauth2client.client import GoogleCredentials

def get_access_token():
    credentials_data = {
        "type": "service_account",
        "project_id": st.secrets["google"]["project_id"],
        "private_key_id": st.secrets["google"]["private_key_id"],
        "private_key": st.secrets["google"]["private_key"].replace("\\n", "\n"),
        "client_email": st.secrets["google"]["client_email"],
        "client_id": st.secrets["google"]["client_id"],
        "auth_uri": st.secrets["google"]["auth_uri"],
        "token_uri": st.secrets["google"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["google"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["google"]["client_x509_cert_url"]
    }
    
    credentials = GoogleCredentials.from_stream(credentials_data)
    credentials = credentials.create_scoped(['https://www.googleapis.com/auth/cloud-platform'])
    return credentials.get_access_token().access_token

st.title('Job Search')

companies = st.multiselect('Select Companies', ['Google', 'Facebook', 'Microsoft'])

url = 'https://jobs.googleapis.com/v2/jobs/search' 

if st.button("Search Jobs"):
    
    headers = {
        'Authorization': f'Bearer {get_access_token()}'
    }
    
    if companies:
        params = {
            'q': 'python developer', 
            'companyNames': ','.join(companies),  
            'location': 'San Francisco, CA'
        }
    else:
        params = {
            'q': 'python developer',  
            'location': 'San Francisco, CA'
        }
      
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        
        if 'jobs' in data:
            for job in data['jobs']:
                st.write(job['title'], job['company'], job['location'])
        else:
            st.write("No jobs found.")

    except requests.exceptions.RequestException as e:
        st.write(f"An error occurred: {e}")
