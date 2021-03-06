import streamlit as st
from components.icons import st_icons
from components.map import st_map
from components.utils import load_data, compute_mean
from components.charts import st_charts, st_charts_line


# List of global var to be shown at the top
list_global_var = [
    "Female share of employment in senior and middle management (%)",
    "Educational attainment, At least Bachelor's or equivalent, population 25+, female (%) (cumulative)",
    "Contraceptive prevalence, Any method (% of married women ages 15-49)",
    "Age at first marriage, Female"]

# Load raw data and aggregated one
raw_data, agg_data = load_data()
raw_data.head()
agg_data.head()

# This command sets the page to full screen
st.set_page_config(layout="wide")

# Test title
st.title('Gender Differences in the World')
st.subheader("An overview on women's employment, education and family health levels around the world")
st.text(" ")
st.text(" ")
st.text(" ")
st.markdown("##### A. Check the Gender Key Indicators Summary:")
st.markdown("_Default values correspond to Global Yearly Means._")

# We compute the global mean to be displayed at the start
global_means = compute_mean(agg_data, list_index = None, list_var = list_global_var)

icons_container = st.empty()

st_icons(global_means, icons_container)
    
st_map(agg_data, list_global_var, icons_container, global_means)

st_charts(agg_data)

st_charts_line(raw_data)

