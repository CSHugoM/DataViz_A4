import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events

from components.utils import compute_mean
from components.icons import st_icons


def st_map(data : pd.DataFrame, list_global_var : list, icons_container, global_means : list):
    
    st.markdown("##### B. Pick one gender key indicator from the dropdown list and visualise it for all countries using the map:")

    general_list = ['Adolescent fertility rate', 
                    'Age at first marriage', 
                    'Cause of death, by communicable diseases and materl, pretal and nutrition conditions',
                    'Cause of death, by non-communicable diseases',
                    'Contraceptive prevalence',
                    'Educational attainment',
                    'Female share of employment in senior and middle magement',
                    'Fertility rate',
                    'Ratio of female to male labor force participation rate',
                    'Wage and salaried workers',
                    'Wanted fertility rate',
                    'Women making their own informed decisions regarding sexual relations, contraceptive use and reproductive health care',
                    'Women who believe a wife is justified refusing sex with her husband if she knows he has sexually transmitted disease'
                    ]
    column_names = list(data.columns)
    initial_variable = st.selectbox('', tuple(general_list))
    new_list = [s for s in column_names if initial_variable in s]
    #if(any(substring in string for substring in substring_list)):
        
    choosen_variable = st.selectbox('', tuple(new_list))
    
    st.markdown("Plus, you can also click or select countries in the map to see the **Gender Key Indicators Summary** for these countries. To revert changes, use the **Reset** button:")

    #refresh button
    if st.button("Reset"):
        raise st.experimental_rerun()

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

