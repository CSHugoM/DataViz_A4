import streamlit as st
from components.icons import st_icons
from components.map import st_map
from components.utils import load_data

raw_data, agg_data = load_data()

st.set_page_config(layout="wide")

st_icons(10, 20, 30, 40)

st_map(agg_data, "Ratio of female to male labor force participation rate (%) (modeled ILO estimate)")
    
