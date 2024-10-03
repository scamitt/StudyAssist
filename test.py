import streamlit as st
import os
from utils import *
from dotenv import load_dotenv

def main():

    st.set_page_config(page_title="Study Material Generator")
    st.title("PDF Summarizing App 📄")
    st.write("Generate study material in just a few seconds!")

    pdf = st.file_uploader("Upload your document",type = 'pdf')

    submit = st.button("Submit")

    load_dotenv()  # Load environment variables from the .env file
    api_key = os.getenv('API_KEY')
    os.environ["OPENAI_API_KEY"] = api_key

    if submit:
        response1,response2 = summarizer(pdf)
        st.subheader("Key topics:")
        st.write(response1)
        st.subheader("Practice Questions")
        st.write(response2)

if __name__ == "__main__":
    main()
