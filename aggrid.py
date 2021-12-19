# https://github.com/PablocFonseca/streamlit-aggrid/blob/main/st_aggrid/__init__.py

from st_aggrid import GridOptionsBuilder ,AgGrid, GridUpdateMode
import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
@st.cache(allow_output_mutation=True)
def fetch_data():
    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    return df


df = fetch_data()
#st.write(df.columns)
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection('single')
gb.configure_selection('multiple', use_checkbox=True, rowMultiSelectWithClick=True, suppressRowDeselection=True)
gb.configure_grid_options(domLayout='normal')
gridOptions = gb.build()
grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
    allow_unsafe_jscode=True, 
    )
#df = grid_response['data']
#st.write(df)
with st.spinner("Displaying results..."):
    st.write(gridOptions)
    selected = grid_response['selected_rows']
    selected = pd.DataFrame(selected)
    st.write(len(grid_response['selected_rows']))
