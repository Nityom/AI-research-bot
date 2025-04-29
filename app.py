import openai
import requests
import json
import streamlit as st
import time

# Azure OpenAI API credentials
API_KEY = "8zQVvmoBZdezoPZKosGdaLrrtoZ6PTzPIqnRIly0j1f1DiCStyliJQQJ99BCACHYHv6XJ3w3AAAAACOGmA8T"
ENDPOINT = "https://nktik-m8hv2vz2-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2025-01-01-preview"

# SerpAPI credentials
SERPAPI_API_KEY = "0d8d867597e09e0dfd0c1ba2215c9f4f9e3d1a52ef4d81bd6c3709d49ea20c52"  # <-- put your SerpAPI key here

# Function to get citations from SerpAPI (Google Scholar)
def get_citations(topic):
    params = {
        "engine": "google_scholar",
        "q": topic,
        "api_key": SERPAPI_API_KEY
    }

    search_url = "https://serpapi.com/search.json"
    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        results = response.json()
        citations = []
        for article in results.get('organic_results', []):
            title = article.get('title')
            link = article.get('link')
            if title and link:
                citations.append((title, link))
        return citations
    else:
        return []

# Function to get response from Azure OpenAI for summarization
def get_ai_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are an assistant for research."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.5,
        "model": "gpt-4"
    }

    response = requests.post(ENDPOINT, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit UI
st.title("📚 Research Citation Summarizer")

# Input field for research topic
topic = st.text_input("🔍 Enter Research Topic:")

if topic:
    with st.spinner("Fetching citations..."):
        # Get citations from Google Scholar (via SerpAPI)
        citations = get_citations(topic)
    
    if citations:
        st.success(f"✅ Found {len(citations)} citations for the topic: **'{topic}'**")

        # Display citations with links
        for citation, link in citations:
            st.markdown(f"🔗 [{citation}]({link})")

        # Summarize citations when the button is clicked
        if st.button("🧠 Summarize Citations"):
            with st.spinner("Summarizing citations with AI..."):
                summaries = []
                for citation, link in citations:
                    # Prepare prompt for AI summarization
                    prompt = f"Summarize the research paper titled: {citation}"
                    summary = get_ai_response(prompt)
                    summaries.append((citation, summary))
                    time.sleep(1)  # Delay to avoid hitting rate limits
            
            # Display summarized content
            st.header("Summaries:")
            for citation, summary in summaries:
                st.subheader(citation)
                st.write(summary)

    else:
        st.warning("⚠️ No citations found. Try a different topic.")
