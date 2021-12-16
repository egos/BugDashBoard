import streamlit as st
import pandas as pd
import requests

url = "http://egosgame.net/file.txt"
r = requests.get(url)
#r.text
#r.text.split(";")
st.write(pd.Series(r.text.split(";")).value_counts())


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
