import streamlit as st # web development
import numpy as np # np mean, np random
import pandas as pd # read csv, df manipulation
import time # To simulate a real time data, time loop
import plotly.express as px # Interactive charts

selected_dataframe = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.set_page_config(
    page_title= 'Real-Time Data Science Dashboard',
    page_icon= "✅"
    layout= "wide"
)

st.title("Real-Time / Live Data Science Dashboard")

