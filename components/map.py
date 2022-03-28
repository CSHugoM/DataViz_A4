import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events

from components.utils import compute_mean
from components.icons import st_icons


def st_map(data : pd.DataFrame, list_global_var : list, icons_container, global_means : list):

    choosen_variable = st.selectbox('', tuple(list(data.columns)))

    fig = go.Figure(data=go.Choropleth(
        locations=data.index,  # Spatial coordinates
        z=data[choosen_variable].astype(float),  # Data to be color-coded
        locationmode='country names',  # set of locations match entries in `locations`
        colorscale='Viridis',
        colorbar_title=choosen_variable,
    ))

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    map_container = st.container()

    with map_container:
        selected_countries = plotly_events(fig, click_event = True, select_event = True)
    
    list_index = [e['pointIndex'] for e in selected_countries]

    if list_index != []:
        st_icons(compute_mean(data, list_index, list_global_var), icons_container)
    else :
        st_icons(global_means, icons_container)

