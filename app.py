"""
# Tutorial: Building data apps with Streamlit
Created by Natkamon Tovanich - version 2022-03-01
"""

import streamlit as st
import pandas as pd
import altair as alt
from altair import datum
from vega_datasets import data
from streamlit_vega_lite import vega_lite_component, altair_component
import time

# Load data

data = pd.read_csv('gender_data_clean.csv', delimiter = ";", header = True)

st.write('# World Development Indicators')

st.write('## 1. Load data')
# Load Gapminder data
# @st.cache decorator skip reloading the code when the apps rerun.


# Use st.write() to render any objects on the web app


# Magic command: Streamlit automatically writes a variable 
# or a literal value to your app using st.write().


# Select year


# Create an Altair chart
st.write('## 2. Create Altair charts on Streamlit')

st.code('''
# Bubble chart with selection
selected = alt.selection_multi(encodings=['x', 'y', 'size'])

chart = alt.Chart(source).mark_circle(opacity=0.7, stroke='black', strokeWidth=1).encode(
    x=alt.X('GDP per capita (current LCU):Q', scale=alt.Scale(type='log', zero=False)),
    y=alt.Y('Life expectancy at birth, total (years):Q', scale=alt.Scale(zero=False)),
    size=alt.Size('Population, total:Q', scale=alt.Scale(range=(30, 3000), zero=False)),
    color=alt.condition(selected, alt.Color('Region:N'), alt.value('lightgray')),
    tooltip='Country'
).add_selection(selected).properties(width=800, height=500).interactive()
''')

# Create the bubble chart with selection


# Showing Altair chart on the apps


st.code('''
# World 
countries = alt.topo_feature(data.world_110m.url, 'countries')

chart = alt.Chart(countries).mark_geoshape(
    stroke='white'
).encode(
    color='CO2 emissions (kt):Q'
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(source, 'id', ['CO2 emissions (kt)'])
).project('equirectangular').properties(
    width=800,
    height=500,
    title='CO2 emissions (kt)'
)''')


# Create the world map chart


# Showing Altair chart on the apps


st.write('## 3. Add user inputs and update the chart')

# What if we can select the variable to display in the chart


# What if we can filter some countries to show on the chart


# Put those inputs on the sidebar


# What if we can see the statistics over the years


# Select the data according to the user inputs


# Add text.markdown() to show the year displayed on the chart


# Plot the bubble chart again as a function with st.cache decorator
@st.cache(allow_output_mutation=True)
def plotBubbleChart(df, keys, global_max=False):

    return None



# What if we can animate the chart to see statistics over the years

# Find the minimum and maximum year for the selected variables
@st.cache()
def minmaxYear(df, x, y):
    temp_x = df[['Year', x]].dropna()
    temp_y = df[['Year', y]].dropna()

    first = max(temp_x['Year'].min(), temp_y['Year'].min())
    last = min(temp_x['Year'].max(), temp_y['Year'].max())
    return (first, last)

# Add start and stop button and animate the chart over the years


# Relate the data between charts
st.write('## 4. Interacting with other Altair charts')

st.code('''
# Connected Scatterplot
source = df[df['Country'].isin(['France', 'Thailand', 'Brazil'])]

chart = alt.Chart(source).mark_line(point=True).encode(
    x=alt.X('GDP per capita (current LCU):Q', scale=alt.Scale(type='log', zero=False)),
    y=alt.Y('Life expectancy at birth, total (years):Q', scale=alt.Scale(zero=False)),
    color='Country:N',
    order='Year',
    tooltip=['Country', 'Year']
).properties(width=800, height=500)''')

# Plot the connected scatterplot
def plotConnectedScatterplot(df, keys, countries):
    source = df[df['Country'].isin(countries)]

    x_scale = alt.Scale(type='log', zero=False) if keys['x_log'] else alt.Scale(zero=False)
    y_scale = alt.Scale(type='log', zero=False) if keys['y_log'] else alt.Scale(zero=False)

    chart = alt.Chart(source).mark_line(point=True).encode(
        x=alt.X('{}:Q'.format(keys['x']), scale=x_scale),
        y=alt.Y('{}:Q'.format(keys['y']), scale=y_scale),
        color='Country:N',
        order='Year',
        tooltip=['Country', 'Year']
    ).properties(width=800, height=500)

    return chart


# Create another chart to related to the bubble chart


# Add the selection to relate bubble chart with the connected scatter plot
#if selection.get("vlMulti"):

    # What is the selection variable?
    
    
    # Convert selection to data frame
    
    
    # Find countries that match the selection
    

    # Plot the connected scatterplot chart
    