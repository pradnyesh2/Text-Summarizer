import streamlit as st
import validators
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import UnstructuredURLLoader,YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat
from langchain_yt_dlp.youtube_loader import YoutubeLoaderDL
from langchain.chains.summarize import load_summarize_chain

## Streamlit app
st.set_page_config(page_title="Text Summarizer",page_icon="📃")
st.title("📃Text Summarizer:Summarize the text from Youtube or Website url")
st.subheader("summarize url:")


## Groq api key
st.sidebar.title("Settings")
groq_api_key=st.sidebar.text_input("Enter your groq api key:",value="",type="password")


## Gemma model to summarize
llm=ChatGroq(model="gemma2-9b-It",api_key=groq_api_key)

prompt_template="""
Provide the summary of following content in 300 words:
Content:{text}
"""

prompt=PromptTemplate(input_variables=['text'],
                      template=prompt_template)

if not groq_api_key:
    st.warning("Please enter groq api")
else:
    generic_url=st.text_input(label="Enter url to summarize",label_visibility="collapsed")
    # st.write(f"URL:{generic_url}")
    
    if not generic_url:
        st.error("Please provide a valid url to get started with summarization")
    elif not validators.url(generic_url):
        st.error("Please enter valid url. It can be youtube url or webside url.")
    else:
        # st.success("Valid URL")
        try:
            with st.spinner("Summarizing..."):
                ## Loading the website and YT video data
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=False)
                    # loader = YoutubeLoaderDL.from_youtube_url(generic_url, add_video_info=False)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()  
                # st.write(docs)
                # st.write(llm.get_num_tokens(docs))

                chain=load_summarize_chain(llm=llm,chain_type="stuff",verbose=True,prompt=prompt)
                # st.write(chain)
                output_summary=chain.run(docs)
                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception:{e}")



    


