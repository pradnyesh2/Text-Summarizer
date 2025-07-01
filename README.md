# 📃 Text Summarizer App
This is a Streamlit-based web application that allows you to summarize content from YouTube videos, websites, or blogs by simply providing their URL. It leverages the power of Large Language Models (LLMs) via the Groq API to generate concise summaries, helping you quickly grasp the main points without consuming the entire content.

## ✨ Features
- YouTube Video Summarization: Get a summary of any YouTube video by providing its URL.
- Website/Blog Summarization: Summarize articles or blog posts from any valid website URL.
- Concise Summaries: Generates summaries of approximately 300 words.
- User-Friendly Interface: Built with Streamlit for a simple and intuitive user experience.
- API Key Integration: Securely input your Groq API key directly within the app's sidebar.

## 🚀 How to Use
- Enter your Groq API Key: In the sidebar on the left, paste your Groq API key into the "Enter your groq api key" field. This is essential for the summarization functionality.
- Provide a URL: In the main section of the app, enter the URL of the YouTube video, website, or blog post you wish to summarize.
- Get Summary: The app will automatically start summarizing the content once a valid URL and API key are provided. The summary will appear below the input field.

## 🛠️ Installation
To run this application locally, follow these steps:

###  Prerequisites
- Python 3.8+
- Groq API Key: You can obtain one from Groq Cloud.

### Setup Steps
Clone the repository (if applicable) or save the code:
If you have the code in a repository, clone it:

git clone <your-repo-url>
cd <your-repo-name>

Otherwise, save the provided Python code as app.py in a new directory.

Create a virtual environment (recommended):

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install the required libraries:

pip install -r requirements.txt

## 🏃 Running the App
Once all dependencies are installed, you can run the Streamlit application from your terminal:

streamlit run streamlit-app.py

This command will open the application in your default web browser.

### 💻 Technologies Used
- Streamlit: For creating the web application interface.
- LangChain: Framework for developing applications powered by language models.
- Groq API: Provides fast inference for large language models (using gemma2-9b-It).
- validators: For URL validation.
- UnstructuredURLLoader: For loading content from general web URLs.
- YoutubeLoader / YoutubeLoaderDL: For loading transcripts from YouTube videos.

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details (if you wish to add one).