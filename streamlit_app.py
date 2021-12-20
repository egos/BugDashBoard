import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.express as px
st.set_page_config(layout="wide")

@st.cache(allow_output_mutation=True)
def load_list():    
    url = "http://egosgame.net/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="lxml").find_all("a")
    FileList = [item['href']  for item in soup if ".json" in item.get('href')]
    return FileList

@st.cache(allow_output_mutation=True)
def load_data(file):    
    #file = 'SAVE_test_0_.json'
    url = "https://egosgame.net/{}".format(file)

    resp = requests.get(url=url)
    data = resp.json() 

    sys = data['systems']
    data.pop('systems', None)

    L = []
    colVal = list(data['log']['log0']['best'].keys())
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

    #df['MaxNbug'] = (df.Nbug.max() - df.Kbug)

    #df = df.pivot( columns="P_log", values='Nbug')
    return df, colVal

FileList = load_list()
file = st.sidebar.radio('save', FileList)
df, colVal = load_data(file)
colP = [c for c in  df.columns if 'P_' in c]
colP = [c  for c in colP  if df[c].nunique()>1]  
#fig = px.line(df)
fig = px.line(df, x="time", y="Nbug", color='P_log')
#fig.show()
st.plotly_chart(fig, use_container_width=True)
#st.write(df)
dfx = df.groupby(colP)[colVal].max().reset_index().set_index('P_log').sort_index()
st.write(dfx)


