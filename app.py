import streamlit as st
import pandas as pd
import plotly.express as px
from llm import coach_llm
from strava_api import return_strava_data
from parser import parsed_run_data
from context import data_context



@st.cache_data(show_spinner=False)
def get_runs():
    return parsed_run_data(return_strava_data())


running_data = get_runs()
df = pd.DataFrame(running_data)



st.title("Running Coach")

with st.sidebar:
    user_question = st.text_input("Ask about your run data")
    if st.button("Ask"):
        with st.spinner("Running to fetch a response ..."):
            parsed_data = get_runs()
            contextual_data = data_context(parsed_data,user_question)
            llm_response = coach_llm(contextual_data)
            st.write(llm_response)






## Pace over time
df['pace_display'] = df['pace'].apply(lambda x: f"{int(x)}:{int((x % 1) * 60):02d}")
st.plotly_chart(px.line(df, x="date", y = "pace", hover_data={"pace": False, "pace_display": True}, title="Pace Over Time"))

## Distance per run
df['distance_display'] = df['distance'].apply(lambda x: x / 1000)
st.plotly_chart(px.line(df, x = "date", y = "distance", title="Distance per run", hover_data={"distance": False, "distance_display": True}))

## Heart rate over time
st.plotly_chart(px.line(df, x="date", y="average_heartrate", title="Heartrate over time"))

## Heart rate vs pace
st.plotly_chart(px.scatter(df, x="pace", y="average_heartrate", title="Heartrate over pace"))