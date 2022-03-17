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
from PIL import Image
import os

from components.icons import st_icons

st_icons()
    
