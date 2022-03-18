import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def st_map(data : pd.DataFrame):

    choosen_variable = st.selectbox('', tuple(list(data.columns)))

    fig = go.Figure(data=go.Choropleth(
        locations=data.index,  # Spatial coordinates
        z=data[choosen_variable].astype(float),  # Data to be color-coded
        locationmode='country names',  # set of locations match entries in `locations`
        colorscale='Viridis',
        colorbar_title=choosen_variable,
    ))

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, width=3000)

    map_container = st.container()

    with map_container:
        st.plotly_chart(fig, use_container_width=True)
