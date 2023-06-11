import os
import streamlit as st 
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))

st.title("🐼 Data analysis with PandasAI 🦥")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

def analyseCSV(df, prompt):
    # create an LLM by instantiating OpenAI object, and passing API token
    llm = OpenAI()

    # create PandasAI object, passing the LLM
    pandas_ai = PandasAI(llm, verbose=True, conversational=True)

    # call pandas_ai.run(), passing dataframe and prompt
    with st.spinner("Generating response..."):
        st.write(pandas_ai.run(df, prompt))

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

    # new code below...
    prompt = st.text_area("Enter your query:")

    # Generate output
    if st.button("Generate"):
        if prompt:
            analyseCSV(df, prompt)
        else:
            st.warning("Please enter a query.")

        