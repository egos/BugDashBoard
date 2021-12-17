# https://github.com/null-jones/streamlit-plotly-events


import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
from streamlit_plotly_events import plotly_events

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

df=[]
df= pd.DataFrame(df)
df['year']= x
df['lifeExp']= y

#fig = px.scatter(df, x="year", y="lifeExp", title='Life expectancy in Canada')
col1, col2 = st.columns(2)
fig = px.imshow([[1, 20, 30],
                 [20, 1, 60],
                 [30, 60, 1]])
# Plot!
#st.plotly_chart(fig, use_container_width=True)
col2.plotly_chart(fig,use_container_width = True)
col1.plotly_chart(fig,use_container_width = True)
selected_points = plotly_events(fig, key= 'a')
if selected_points : 
    a = selected_points[0]
    a = pd.DataFrame.from_dict(a,orient='index')
    st.write(selected_points)