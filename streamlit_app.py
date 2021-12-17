import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.express as px

url = "http://egosgame.net/"
r = requests.get(url)
soup = BeautifulSoup(r.text).find_all("a")
FileList = [item['href']  for item in soup if ".json" in item.get('href')]
st.write(FileList)


file = 'SAVE_test_0_.json'
url = "https://egosgame.net/{}".format(file)

resp = requests.get(url=url)
data = resp.json() 

sys = data['systems']
data.pop('systems', None)

L = []
len(data.items())
for k,v in data['log'].items():
    params = v['params']
    val = v['val']
    df = pd.DataFrame(val)
    df.index = df.index.astype(int)
    df.insert(0, 'P_log', int(k.replace("log", "")))
    col = ['P_'+k for k in params.keys()]
    for k, v in params.items(): 
        df.insert(0, 'P_'+k, v)
    L.append(df)

df = pd.concat(L, sort = False).fillna(0).astype(int)

df['MaxNbug'] = (df.Nbug.max() - df.Kbug)

df = df.pivot( columns="P_log", values='Nbug')
fig = px.line(df)
st.plotly_chart(fig, use_container_width=True)



