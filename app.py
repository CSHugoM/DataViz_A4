import streamlit as st
from components.icons import st_icons
from components.map import st_map
from components.utils import load_data, compute_mean
from components.charts import st_charts


# List of global var to be shown at the top
list_global_var = [
    "Female share of employment in senior and middle magement (%)",
    "Educatiol attainment, at least Bachelor's or equivalent, population 25+, female (%) (cumulative)",
    "Contraceptive prevalence, any method (% of married women ages 15-49)",
    "Age at first marriage, female"]

# Load raw data and aggregated one
raw_data, agg_data = load_data()

# This command sets the page to full screen
st.set_page_config(layout="wide")

# Test title
st.title('Gender Differences in the World')
st.subheader("An overview on the context and evolution of women's health, employment and education levels")
st.text(" ")
st.text(" ")
st.text(" ")

# We compute the global mean to be displayed at the start
global_means = compute_mean(agg_data, list_index = None, list_var = list_global_var)

icons_container = st.empty()

st_icons(global_means, icons_container)

#refresh button
if st.button("Reset"):
    raise st.experimental_rerun()
    
st_map(agg_data, list_global_var, icons_container, global_means)

st_charts(agg_data)


