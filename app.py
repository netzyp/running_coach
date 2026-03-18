import streamlit as st
from llm import coach_llm
from strava_api import return_strava_data
from parser import parsed_run_data
from context import data_context



@st.cache_data(show_spinner=False)
def get_runs():
    return parsed_run_data(return_strava_data())






st.title("Running Coach")

with st.sidebar:
    with st.spinner("Running to fetch a response ..."):
        user_question = st.text_input("Ask about your run data")
        if st.button("Ask"):
            parsed_data = get_runs()
            contextual_data = data_context(parsed_data,user_question)
            llm_response = coach_llm(contextual_data)
            st.write(llm_response)






    