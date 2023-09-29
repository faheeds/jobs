import streamlit as st
import requests 

st.title('Job Search')

companies = st.multiselect('Select Companies', ['Google', 'Facebook', 'Microsoft'])

url = 'https://jobs.googleapis.com/v2/jobs/search' 

API_KEY = st.secrets["google"]["api_key"]  # Make sure you have added "api_key" in your secrets.toml under [google]

if st.button("Search Jobs"):
    
    if companies:
        params = {
            'q': 'python developer', 
            'companyNames': ','.join(companies),  
            'location': 'San Francisco, CA',
            'key': API_KEY  # The API key is sent as a parameter in the request
        }
    else:
        params = {
            'q': 'python developer',  
            'location': 'San Francisco, CA',
            'key': API_KEY  # The API key is sent as a parameter in the request
        }
      
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        
        if 'jobs' in data:
            for job in data['jobs']:
                st.write(job['title'], job['company'], job['location'])
        else:
            st.write("No jobs found.")

    except requests.exceptions.RequestException as e:
        st.write(f"An error occurred: {e}")
