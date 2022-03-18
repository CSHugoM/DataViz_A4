import plotly.express as px
import pandas as pd
import streamlit as st

def st_charts(data : pd.DataFrame):

    cols = st.columns(2)

    choosen_variable_1 = cols[0].selectbox('', tuple(list(data.columns)), key = "1")
    choosen_variable_2 = cols[1].selectbox('', tuple(list(data.columns)), key = "2")

    chart = px.scatter(data, x=choosen_variable_1, y = choosen_variable_2, text=data.index)

    chart.update_traces(textposition='top center')

    char_container = st.container()

    with char_container:
        st.plotly_chart(chart, use_container_width=True)
