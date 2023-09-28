import streamlit as st
from google.auth import default

# Import Talent API client 
from google.cloud import talent_v4 as talent
from google.cloud.talent_v4 import enums
from google.cloud.talent_v4 import types

# Page config
st.set_page_config(page_title='Job Search', page_icon=':mag:')

# Title  
st.title('Job Search App')

# Company input
company = st.text_input('Enter a company name to search jobs') 

if company:

  # GCP Credentials
  creds, _ = default()

  # Initialize client
  client = talent.JobServiceClient(credentials=creds)

  # Build request
  request = talent.ListJobsRequest(
      parent='projects/my-project/tenants/my-tenant',
      filter=f'companyName="{company}"'
  )

  # Call API
  response = client.list_jobs(request=request)

  # Display results
  for job in response:
    st.write(f"**{job.job_title}** at {job.company_name}")
