import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

from PIL import Image
from urllib.request import urlopen
import json

df = pd.read_excel('src/SASB.xlsx', sheet_name= 0)
df1 = pd.read_excel('src/SASB.xlsx', sheet_name= 1)
df_note = pd.read_csv('src/notation.csv')

list_industry = df['Industry'].unique().tolist()

score_A = Image.open('src/Score_A.png')
score_B = Image.open('src/Score_B.png')
score_C = Image.open('src/Score_C.png')
score_D = Image.open('src/Score_D.png')
score_E = Image.open('src/Score_E.png')


def to_colours(chiffre):
    if chiffre >= 80:
        return '#00FF6A'
    elif chiffre < 80 and chiffre >= 60:
        return '#FFD300'
    elif chiffre < 60 and chiffre >= 40:
        return '#FF9900'
    elif chiffre < 40 and chiffre >= 20:
        return '#FF0A00'
    elif chiffre < 20 and chiffre >= 00:
        return '#AC00FF'

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

st.header('Indice de Maturité Environnemental :')

col1, col2 = st.columns(2)

with col1:
    option = st.selectbox(
        'What is your sector?',
        (list_industry))
    # st.write('You selected:', option)

    # Depuis la selection de Menu déroulant
    select = df[ df['Industry'] == str(option) ].reset_index()

    select1 = df1[ df1['Industry'] == str(option) ].reset_index()
    select1 = select1[ select1['Accounting Metric Category'] == 'Discussion and Analysis'].reset_index()

    select_note = df_note[ df_note['Industry'] == str(option) ].reset_index()

with col2:
    #if st.button('Say hello'):
    #    st.write('Why hello there')
    #else:
    #    st.write('Goodbye')
    st.write(' ')


with col1:
    # st.title('This is a plot :')
    cli = select_note['Climate Change'][0]
    pol = select_note['Pollution'][0]
    wat = select_note['Water and Marine Resources'][0]
    bio = select_note['Biodiversity and Ecosystems'][0]
    cir = select_note['Circular Economy'][0]

    df = pd.DataFrame(dict(
        r=[cli, pol, wat, bio, cir],
        theta=['Climate Change','Pollution','Water and Marine Resources',
            'Biodiversity and Ecosystems', 'Circular Economy']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.title(' ')
    st.text('')
    st.subheader('Scores :')
    scol1, scol2, scol3, scol4, scol5 = st.columns(5)

    with scol1:
        cli_o = select_note['Climate Change_Ordinal'][0]
        st.image(Image.open(f'src/Score_{cli_o}.png'), caption='Climate Change')

    with scol2:
        pol_o = select_note['Pollution_Ordinal'][0]
        st.image(Image.open(f'src/Score_{pol_o}.png'), caption='Pollution')

    with scol3:
        wat_o = select_note['Water and Marine Resources_Ordinal'][0]
        st.image(Image.open(f'src/Score_{wat_o}.png'), caption='Water and Marine Resources')

    with scol4:
        bio_o = select_note['Biodiversity and Ecosystems_Ordinal'][0]
        st.image(Image.open(f'src/Score_{bio_o}.png'), caption='Biodiversity and Ecosystems')

    with scol5:
        cir_o = select_note['Circular Economy_Ordinal'][0]
        st.image(Image.open(f'src/Score_{cli_o}.png'), caption='Circular Economy')

    scol6, scol7 = st.columns(2)

    note = select_note['Globals_Ordinal'][0]
    score_global = select_note['Globals'][0]
    score_gcolor = to_colours(score_global)

    components.html(f"""
    <div style="display: flex; width: 400px; height: 100px; background-color: #f2f2f2; border-radius: 40px; margin: auto;">
        <div style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <p style="margin: 0; font-size: 14px; font-weight: medium; color: #31333f; font-family: 'Source Sans Pro', sans-serif;">Global Score</p>
            <p style="margin: 0; font-size: 2.25rem; color: #31333f; font-family: 'Source Sans Pro', sans-serif;">{score_global}/100</p>
        </div>
        <div style="flex: 1; background-color: white; border: 4px solid {score_gcolor}; display: flex; align-items: center; justify-content: center; border-top-right-radius: 40px; border-bottom-right-radius: 40px;">
            <p style="margin: 0; color: {score_gcolor}; font-size: 2.25rem; font-weight: 700; font-family: 'Source Sans Pro', sans-serif;">{note}</p>
        </div>
    </div>
    """)
    
col1bis, col2bis = st.columns(2)



with col1bis:
    st.subheader('Disclosure Topic :')

    for i in range(len(select)):
        expander = st.expander(select['Disclosure Topic'][i])
        expander.write(select['Disclosure Topic Description'][i])

with col2bis:
    st.subheader('Questions :')

    for i in range(len(select1)):
        expander = st.expander(select1['Accounting Metric Category'][i])
        expander.write(select1['Accounting Metric'][i])
        

st.subheader('Map of emissions:')

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                 dtype={"fips": str})

fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)