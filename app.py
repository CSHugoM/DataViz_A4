import streamlit as st
from components.icons import st_icons
from components.map import st_map
from components.utils import load_data
from components.charts import st_charts

raw_data, agg_data = load_data()

st.set_page_config(layout="wide")

st_icons(10, 20, 30, 40)

st_map(agg_data)

st_charts(agg_data)


