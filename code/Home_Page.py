from crawl_SQLinterface import read_to_df, read_to_query
import streamlit as st
import requests
import pandas as pd

cafe = read_to_query("cafe")
cafe_rating = read_to_query("cafe_rating")
cafe_features = read_to_query("cafe_features")

st.title("Iran Resturants Analysis")
st.subheader('welcome to our project :)')

"""
### In this document we'll answer the following questions:


- What features can have a effect on the rate of cafe?
- Is the place of cafe have an impact on rating?  
- Do food quality and service quality and etc. rates have a meaningful relation with rate of the cafe?
- Does time of work affect the cafe business? 


""" 
st.markdown("<h3 style='text-align: center;'>Count of cafes in each city</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

df = read_to_df('cafe').groupby('city').count().cafe_id.rename('Count')
df = df.sort_values(ascending=False)
df.index = [x.title() for x in df.index]
col1.dataframe(df)

col2.line_chart(df)

'''
**click on [link](https://github.com/Mmli081/Iran-restaurant-analyzer/tree/develop) to access our project on github**

hope you enjoy it...
'''
