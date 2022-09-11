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
st.subheader('Time')

st.subheader('Features')
Features = st.multiselect(
    "Features You Like ?!",
    ('قلیان','اینترنت رایگان','ارسال رایگان (Delivery)','سیگار','فضای باز','موسیقی زنده','پارکینگ', 'دستگاه کارت خوان'),
    ('اینترنت رایگان'))
st.write('Cafe should have : \n\n'+",".join(Features))

city = st.selectbox(
    "select one or more city",
    ('sabzevar', 'bandarabbas', 'tehran', 'qazvin', 'urmia', 'kish',
       'karaj', 'ahwaz', 'tabriz', 'isfahan', 'zanjan', 'arak', 'hamedan',
       'kerman', 'ghom', 'mashhad', 'shiraz'))

cost = st.radio(
    "what price range do you ?",
    ("cheap","economical","expensive","costly"),
    index= 2)

mohalat = tuple(get_mohalat())
province = st.selectbox(
    'what province you want your cafe to be in?',
    mohalat,
    98
)
yes = st.checkbox("only show open cafe")
t = datetime.now().time()

# q = read_to_query('cafe',filter=isopen(t))
# q = read_to_query(q,filter=isopen(t))




if yes:
    q = read_to_query('cafe',filter=isopen(t))
else : q = None
