from signal import signal
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_SQLinterface import *

st.header("Displaying & Plotting")

################################################################################

st.subheader("Distribution of rate")

rate_kind = st.selectbox(
    "Choose a kind of rate", 
    ['food_quality','service_quality','cost','cost_value','environment','All'])

st.bar_chart(bar_plot_rate(rate_kind))
################################################################################
st.subheader("Distribution of rate in different cities")

cities = st.multiselect(
    "select one or more city",
    ('sabzevar', 'bandarabbas', 'tehran', 'qazvin', 'urmia', 'kish',
       'karaj', 'ahwaz', 'tabriz', 'isfahan', 'zanjan', 'arak', 'hamedan',
       'kerman', 'ghom', 'mashhad', 'shiraz'),
    ("tehran")
)

rate_kind2 = st.selectbox(
    "Choose a kind of rate you want to check in city/cities", 
    ['food_quality','service_quality','cost','cost_value','environment','All'])

st.bar_chart(bar_plot_rate_by_city(rate_kind2,cities))
# ################################################################################

st.subheader('Distribution of rate by different features')
Features = st.multiselect(
    "Features that cafe should have?!",
    ('قلیان','اینترنت رایگان','ارسال رایگان (Delivery)','سیگار','فضای باز','موسیقی زنده','پارکینگ', 'دستگاه کارت خوان'),
    ('دستگاه کارت خوان')
)
rate_kind3 = st.selectbox(
    "Choose a kind of rate you want to check in by", 
    ['food_quality','service_quality','cost','cost_value','environment','All'])

st.bar_chart(bar_plot_rate_by_features(rate_kind3,Features))

# ################################################################################