import streamlit as st # web development
import numpy as np # np mean, np random
import pandas as pd # read csv, df manipulation
import time # To simulate a real time data, time loop
import plotly.express as px # Interactive charts

selected_df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.set_page_config(
    page_title= 'Real-Time Data Science Dashboard',
    page_icon= "✅",
    layout= "wide"
)
# Dashboard Titile
st.title("Real-Time / Live Data Science Dashboard")

# Top-level filters
job_filter = st.selectbox("Select the Job", pd.unique(selected_df['job']))

# creating a singel-element container.
placeholder = st.empty()

selected==_df= selected_df[selected_df['job']] == job_filter


for seconds in range(200):
    
    # Since our csv is static data we want to create a near real time which changes values
    selected_df['age_new'] = selected_df['age'] * np.random.choice(range(1,5))
    selected_df['balance_new'] = selected_df['balance'] * np.random.choice(range(1,5))
    
    avg_age = np.mean(selected_df['age_new'])
    
    