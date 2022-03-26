import plotly.express as px
import pandas as pd
import streamlit as st
import scipy
from scipy import stats


def st_charts(data : pd.DataFrame):

    cols = st.columns([1,2])
    cols[0].write("#")
    cols[0].write("#")
    cols[0].text("Variable 1")
    choosen_variable_1 = cols[0].selectbox('', tuple(list(data.columns)), key = "1")
    cols[0].write("#")
    cols[0].text("Variable 2")
    choosen_variable_2 = cols[0].selectbox('', tuple(list(data.columns)), key = "2")
    cols[0].write("#")
    df = data[[choosen_variable_1,choosen_variable_2]]
    df = df.dropna()
    if choosen_variable_1 == choosen_variable_2:
        r = (1.00,1.00)
    else:
        r =  scipy.stats.pearsonr(df[choosen_variable_1],df[choosen_variable_2])
    r_report = "Correlation: " + str(round(r[0],2))
    cols[0].text(r_report)
    chart = px.scatter(data,x=choosen_variable_1, y = choosen_variable_2, trendline="ols")
    chart.update_traces(textposition='top center')
    chart.update_layout(height = 800, width = 800)

    cols[1].plotly_chart(chart, use_container_width=False)   
    

    
    
