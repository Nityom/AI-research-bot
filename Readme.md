# Research Citation Summarizer

This project is an AI-powered research assistant that helps researchers quickly find relevant citations and summarize them using OpenAI's GPT model. It is built with Python, Streamlit for the user interface, and the Azure OpenAI API to power the chatbot.

## Live Link : https://ai-research-agentt.streamlit.app/

## Features

- **Topic Input**: Enter a research topic to find relevant citations.
- **Citations Extraction**: The app fetches citations related to the given topic from Google Scholar.
- **Summarization**: Use the Azure OpenAI API to summarize the fetched research paper citations.
- **Streamlit Interface**: An interactive and easy-to-use interface that displays citations and their summaries.

## Prerequisites

- [Azure OpenAI API Key](https://azure.microsoft.com/en-us/services/cognitive-services/openai/) - You will need an Azure OpenAI API key to use GPT models.
- Python 3.7+.

## Setup and Installation

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/Nityom/AI-research-bot
```
## 2. Install Dependencies
Make sure to install the required Python packages. Run the following command in your terminal:


pip install -r requirements.txt
Requirements:

openai – To interact with the OpenAI API.

requests – For making HTTP requests to the web for citations.

beautifulsoup4 – For scraping web pages.

streamlit – For building the user interface.

If you don't have a requirements.txt, you can manually install the dependencies:


pip install openai requests streamlit beautifulsoup4
### 3. Get API Key
You need to set up your Azure OpenAI API key. You can sign up for Azure and obtain the key from the Azure portal.

Once you have the API key, replace the placeholder API_KEY in the Python script with your actual key:


API_KEY = "your-new-azure-api-key"
### 4. Run the Application
Once the dependencies are installed and the API key is set, you can run the Streamlit application:



streamlit run research_chatbot.py
This will start a local server, and you can access the app in your browser at http://localhost:8501.

How It Works
Enter a Research Topic: You type a research topic in the input field.

Fetch Citations: The app scrapes Google Scholar for citations related to the given topic.

Summarize Citations: After fetching the citations, click the "Summarize Citations" button, and the app will use the Azure OpenAI API to summarize the citation content.

View Results: The citations along with their summaries will be displayed on the interface.

Example Use Case
Topic: "AI advancements in cybersecurity"

Citations: The app fetches citations from Google Scholar related to the topic.

Summarization: After clicking "Summarize Citations," the app uses GPT to summarize each citation and displays the summarized text.

Security
For security reasons, do not share your API key publicly. Store your API key in a secure manner, such as environment variables or secret management tools. Regenerate your API key if it is accidentally exposed.

License
This project is open-source under the MIT License.

Contact
For any questions or feedback, feel free to contact the project maintainers via GitHub issues or email.

Note: Google Scholar scraping is used in this demo, but it's advisable to use more reliable academic APIs (e.g., CrossRef, PubMed) for a production environment.
