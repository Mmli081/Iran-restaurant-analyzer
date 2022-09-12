# from msilib.schema import Feature
import streamlit as st
import requests
import pandas as pd
from datetime import time, datetime
from streamlit_SQLinterface import *

st.title("Display Tables")

################################################################################



################################################################################
st.header("Filters")
filter =st.checkbox("if you wanna filter it check the box:)")
if filter:
    st.subheader('Time')
    yes = st.checkbox("only show open cafe")
    t = datetime.now().time()
    st.subheader('City')
    city = st.selectbox(
        "select one or more city",
        ('sabzevar', 'bandarabbas', 'tehran', 'qazvin', 'urmia', 'kish',
           'karaj', 'ahwaz', 'tabriz', 'isfahan', 'zanjan', 'arak', 'hamedan',
           'kerman', 'ghom', 'mashhad', 'shiraz')
           ,2)
    st.subheader('Cost')
    cost = st.radio(
        "what price range do you ?",
        ("cheap","economical","expensive","costly"),
        index= 2)
    match cost:
        case "cheap": cost_value = 1
        case "economical": cost_value = 2
        case "expensive":  cost_value = 3
        case "costly": cost_value = 4
    if city=='tehran':
        st.subheader('Province')
        mohalat = tuple(get_mohalat())
        province = st.selectbox(
            'what province you want your cafe to be in?',
            mohalat,
            98)

    st.subheader('Features')
    Features = st.multiselect(
        "Features You Like ?!",
        ('قلیان','اینترنت رایگان','ارسال رایگان (Delivery)','سیگار','فضای باز','موسیقی زنده','پارکینگ', 'دستگاه کارت خوان'),
        ('اینترنت رایگان'))
    st.write('Cafe should have : \n\n'+",".join(Features))

    if yes:
        q = read_to_query('cafe',filter=isopen(t))
        #TODO
        q = read_to_query('cafe',filter=filter_by_city(city))
        q = read_to_query(q,filter=filter_by_range_cost(cost_value))
        if city=='tehran':    
            q = read_to_query(q,filter=filter_by_province(province))
    else :
        q = read_to_query('cafe',filter=filter_by_city(city))
        q = read_to_query(q,filter=filter_by_range_cost(cost_value))
        if city=='tehran':
            q = read_to_query(q,filter=filter_by_province(province))
    df = read_to_df(q)
    show = df[df.cafe_id.isin(has_features(Features).cafe_id)]
    st.dataframe(show)
else :
    st.dataframe(read_to_df("cafe"))