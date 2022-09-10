from msilib.schema import Feature
import streamlit as st
import requests
import pandas as pd

st.title("Display Tables")

################################################################################



################################################################################
st.header("Filters")
st.subheader('Time')
from datetime import time, datetime
opening_time = st.slider(
    "Cafe opening time:",
    value=(time(6, 0), time(21, 0)))

st.subheader('Features')
Features = st.multiselect(
    "Features You Like ?!",
    ('hookah', 'internet', 'delivery','smoking', 'open_space', 'live_music', 'parking', 'pos'),
    ("pos")
)
st.write('Cafe should have : \n\n'+",".join(Features))
