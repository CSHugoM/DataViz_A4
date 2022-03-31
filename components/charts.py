import plotly.express as px
import pandas as pd
import streamlit as st
import scipy
from scipy import stats
import numpy as np
def st_charts(data : pd.DataFrame):
    
    st.markdown("##### C. Explore the statistics and correlations between two key indicators using this scatter plot:")
    st.markdown("_Each mark in the graph corresponds to a different country._")

    cols = st.columns([1,2])
    cols[0].write("#")
    cols[0].markdown("### **Variable 1 (x-Axis)**")
    choosen_variable_1 = cols[0].selectbox('', tuple(list(data.columns)), key = "1")
    reduced_list = list(data.columns)
    reduced_list.remove(choosen_variable_1)
    cols[0].write("#")
    cols[0].markdown("### **Variable 2 (y-Axis)**")
    choosen_variable_2 = cols[0].selectbox('', tuple(reduced_list), key = "2")
    cols[0].write("#")
    df = data[[choosen_variable_1,choosen_variable_2]]
    df = df.dropna()
    if choosen_variable_1 == choosen_variable_2:
        r = (1.00,1.00)
    else:
        r =  stats.pearsonr(df[choosen_variable_1],df[choosen_variable_2])
    r_report = "##### Correlation: " + str(round(r[0],2))
    
    name1 = ""
    c = 1
    for i, letter in enumerate(choosen_variable_1):
        if letter == " ":
           c += 1
        if c % 10 == 0:
            name1 += "<br>"
            c =+ 1
        name1 += letter
        
    name2 = ""
    c = 1
    for i, letter in enumerate(choosen_variable_2):
        if letter == " ":
           c += 1
        if c % 10 == 0:
            name2 += "<br>"
            c =+ 1
        name2 += letter
    
    cols[0].markdown("##### Variable 1:")
    mean1 = "Mean: " + str(round(np.mean(df[choosen_variable_1]),2))
    cols[0].markdown(mean1)
    std1 = "Standard Deviation: " + str(round(np.std(df[choosen_variable_1]),2))
    cols[0].markdown(std1)
    
    cols[0].text(" ")
    
    cols[0].markdown("##### Variable 2:")
    mean2 = "Mean: " + str(round(np.mean(df[choosen_variable_2]),2))
    cols[0].markdown(mean2)
    std2 = "Standard Deviation: " + str(round(np.std(df[choosen_variable_2]),2))
    cols[0].markdown(std2)
    
    cols[0].write("##### ")
    
    cols[0].markdown(r_report)
    
    
    
    
    
    
    chart = px.scatter(data,x=choosen_variable_1, y = choosen_variable_2, trendline="ols",
                       labels={choosen_variable_1:name1,choosen_variable_2:name2},trendline_color_override="red")
    chart.update_traces(textposition='top center')
    chart.update_layout(height = 800, width = 800)

    cols[1].plotly_chart(chart, use_container_width=False)   
    
def st_charts_line(data : pd.DataFrame):
    
    st.markdown("##### D. Visualize how a certain key indicator from the dropdown list evolved in the past ten years")
    st.markdown("_To select specific countries in the visualization, click twice over a country's legend line. To remove a country from visualization, click once over this country's legend line._")
    
    #set-up
    cols = st.columns([1,2])
    cols[0].write("#")
    cols[0].markdown("###### Variable selection:")
    
    variables_list = list(data.drop(['Year','Country'], axis=1).columns)
    choosen_variable_1 = cols[0].selectbox('', tuple(variables_list), key = "1")
    reduced_list = list(data.columns)
    reduced_list.remove(choosen_variable_1)
    cols[0].write("#")
    df = data[['Year',choosen_variable_1]]
    data2 = data.dropna(how='all', axis=0)
    data3 = data2.dropna(how='all', axis=1)
    
    chart = px.line(data3,x='Year', y = choosen_variable_1, color = 'Country')
    # chart.update_traces(textposition='top center')
    chart.update_layout(height = 800, width = 800)

    cols[1].plotly_chart(chart, use_container_width=False, click_event = True)   
    
    

    
    
