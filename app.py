import openai
import requests
import json
import streamlit as st
from bs4 import BeautifulSoup
import time

# Azure OpenAI API credentials
API_KEY = "8zQVvmoBZdezoPZKosGdaLrrtoZ6PTzPIqnRIly0j1f1DiCStyliJQQJ99BCACHYHv6XJ3w3AAAAACOGmA8T"
ENDPOINT = "https://nktik-m8hv2vz2-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2025-01-01-preview"

# Set OpenAI API Key
openai.api_key = API_KEY

# Function to get citations (using Google Scholar as a simple example)
def get_citations(topic):
    search_url = f'https://scholar.google.com/scholar?q={topic}'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    citations = []
    for item in soup.find_all('h3', {'class': 'gs_rt'}):
        citation = item.text
        link = item.find('a')['href']
        citations.append((citation, link))
    
    return citations

# Function to get response from Azure OpenAI for summarization
def get_ai_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are an assistant for research."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.5
    }

    response = requests.post(ENDPOINT, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit UI
st.title("Research Citation Summarizer")

# Input field for research topic
topic = st.text_input("Enter Research Topic:")

if topic:
    with st.spinner("Fetching citations..."):
        # Get citations from Google Scholar
        citations = get_citations(topic)
    
    if citations:
        st.write(f"Found {len(citations)} citations for the topic '{topic}'")

        # Display citations with links
        for citation, link in citations:
            st.markdown(f"[{citation}]({link})")

        # Summarize citations when the button is clicked
        if st.button("Summarize Citations"):
            with st.spinner("Summarizing citations..."):
                summaries = []
                for citation, link in citations:
                    # Prepare prompt for AI summarization
                    prompt = f"Summarize the content of this research paper: {citation}"
                    summary = get_ai_response(prompt)
                    summaries.append((citation, summary))
                    time.sleep(1)  # Add delay to avoid hitting the rate limit
            
            # Display summarized content
            for citation, summary in summaries:
                st.subheader(citation)
                st.write(summary)

    else:
        st.warning("No citations found. Try a different topic.")
