import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "http://egosgame.net/file.txt"
r = requests.get(url)
#r.text
#r.text.split(";")
st.write(pd.Series(r.text.split(";")).value_counts())

url = "http://egosgame.net/"
r = requests.get(url)
soup = BeautifulSoup(r.text).find_all("a")
FileList = [item['href']  for item in soup if ".json" in item.get('href')]
st.write(FileList)


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
