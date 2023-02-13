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

score_A = Image.open('src/Score_A.png')
score_B = Image.open('src/Score_B.png')
score_C = Image.open('src/Score_C.png')
score_D = Image.open('src/Score_D.png')
score_E = Image.open('src/Score_E.png')

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

st.header('Indice de Maturité Environnemental :')

col1, col2 = st.columns(2)

with col1:
    option = st.selectbox(
        'What is your sector?',
        ('XXXXXXX', 'YYYYYYYY', 'ZZZZZZZZ'))
    # st.write('You selected:', option)

with col2:
    #if st.button('Say hello'):
    #    st.write('Why hello there')
    #else:
    #    st.write('Goodbye')
    st.write(' ')


with col1:
    # st.title('This is a plot :')

    df = pd.DataFrame(dict(
        r=[1, 5, 2, 2, 3],
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
        st.image(score_A, caption='Climate Change')
    with scol2:
        st.image(score_B, caption='Pollution')
    with scol3:
        st.image(score_C, caption='Water and Marine Resources')
    with scol4:
        st.image(score_D, caption='Biodiversity and Ecosystems')
    with scol5:
        st.image(score_E, caption='Circular Economy')

    scol6, scol7 = st.columns(2)

    note = 'C'
    score_global = 98 
    score_gcolor = 'orange'

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

    expander = st.expander("Management of Chemicals in Products")
    expander.write('The introduction of the Consumer Product Safety Improvement Act in the U.S. and the Registration, Evaluation, Authorization, and Restriction of Chemicals legislation in the EU demonstrates increasing regulatory and stakeholder concern surrounding the use of harmful or potentially harmful substances in consumer products, including apparel, accessories, and footwear. Finished apparel and footwear products have been found to contain traces of chemicals that have been banned or regulated. Depending on the chemical, the amount present in a product, and the type of exposure that consumers face, specific substances can be carcinogenic, and can disrupt hormone activity in humans and other organisms. Failure to manage this issue may generate additional regulatory oversight and impact a company’s social license to operate. In addition, the presence of harmful chemicals in products can lead to recalls, litigation, and reputational damage. Companies in this industry can work in both the design and manufacturing phases to manage the use of chemicals of concern, develop safe alternatives, and eliminate those that have been banned. Given the industry’s reliance on outsourced manufacturing, this involves proactive partnerships with suppliers. In managing this issue, companies must balance the hazard posed to consumers presented by certain chemicals with the quality of a product and its costs of production.')

    expander = st.expander("Management of Chemicals in Products")
    expander.write('The introduction of the Consumer Product Safety Improvement Act in the U.S. and the Registration, Evaluation, Authorization, and Restriction of Chemicals legislation in the EU demonstrates increasing regulatory and stakeholder concern surrounding the use of harmful or potentially harmful substances in consumer products, including apparel, accessories, and footwear. Finished apparel and footwear products have been found to contain traces of chemicals that have been banned or regulated. Depending on the chemical, the amount present in a product, and the type of exposure that consumers face, specific substances can be carcinogenic, and can disrupt hormone activity in humans and other organisms. Failure to manage this issue may generate additional regulatory oversight and impact a company’s social license to operate. In addition, the presence of harmful chemicals in products can lead to recalls, litigation, and reputational damage. Companies in this industry can work in both the design and manufacturing phases to manage the use of chemicals of concern, develop safe alternatives, and eliminate those that have been banned. Given the industry’s reliance on outsourced manufacturing, this involves proactive partnerships with suppliers. In managing this issue, companies must balance the hazard posed to consumers presented by certain chemicals with the quality of a product and its costs of production.')

    expander = st.expander("Management of Chemicals in Products")
    expander.write('The introduction of the Consumer Product Safety Improvement Act in the U.S. and the Registration, Evaluation, Authorization, and Restriction of Chemicals legislation in the EU demonstrates increasing regulatory and stakeholder concern surrounding the use of harmful or potentially harmful substances in consumer products, including apparel, accessories, and footwear. Finished apparel and footwear products have been found to contain traces of chemicals that have been banned or regulated. Depending on the chemical, the amount present in a product, and the type of exposure that consumers face, specific substances can be carcinogenic, and can disrupt hormone activity in humans and other organisms. Failure to manage this issue may generate additional regulatory oversight and impact a company’s social license to operate. In addition, the presence of harmful chemicals in products can lead to recalls, litigation, and reputational damage. Companies in this industry can work in both the design and manufacturing phases to manage the use of chemicals of concern, develop safe alternatives, and eliminate those that have been banned. Given the industry’s reliance on outsourced manufacturing, this involves proactive partnerships with suppliers. In managing this issue, companies must balance the hazard posed to consumers presented by certain chemicals with the quality of a product and its costs of production.')

with col2bis:
    st.subheader('Questions :')

    expander = st.expander("Management of Chemicals in Products")
    expander.write('The introduction of the Consumer Product Safety Improvement Act in the U.S. and the Registration, Evaluation, Authorization, and Restriction of Chemicals legislation in the EU demonstrates increasing regulatory and stakeholder concern surrounding the use of harmful or potentially harmful substances in consumer products, including apparel, accessories, and footwear. Finished apparel and footwear products have been found to contain traces of chemicals that have been banned or regulated. Depending on the chemical, the amount present in a product, and the type of exposure that consumers face, specific substances can be carcinogenic, and can disrupt hormone activity in humans and other organisms. Failure to manage this issue may generate additional regulatory oversight and impact a company’s social license to operate. In addition, the presence of harmful chemicals in products can lead to recalls, litigation, and reputational damage. Companies in this industry can work in both the design and manufacturing phases to manage the use of chemicals of concern, develop safe alternatives, and eliminate those that have been banned. Given the industry’s reliance on outsourced manufacturing, this involves proactive partnerships with suppliers. In managing this issue, companies must balance the hazard posed to consumers presented by certain chemicals with the quality of a product and its costs of production.')

    expander = st.expander("Management of Chemicals in Products")
    expander.write('The introduction of the Consumer Product Safety Improvement Act in the U.S. and the Registration, Evaluation, Authorization, and Restriction of Chemicals legislation in the EU demonstrates increasing regulatory and stakeholder concern surrounding the use of harmful or potentially harmful substances in consumer products, including apparel, accessories, and footwear. Finished apparel and footwear products have been found to contain traces of chemicals that have been banned or regulated. Depending on the chemical, the amount present in a product, and the type of exposure that consumers face, specific substances can be carcinogenic, and can disrupt hormone activity in humans and other organisms. Failure to manage this issue may generate additional regulatory oversight and impact a company’s social license to operate. In addition, the presence of harmful chemicals in products can lead to recalls, litigation, and reputational damage. Companies in this industry can work in both the design and manufacturing phases to manage the use of chemicals of concern, develop safe alternatives, and eliminate those that have been banned. Given the industry’s reliance on outsourced manufacturing, this involves proactive partnerships with suppliers. In managing this issue, companies must balance the hazard posed to consumers presented by certain chemicals with the quality of a product and its costs of production.')

    expander = st.expander("Management of Chemicals in Products")
    expander.write('The introduction of the Consumer Product Safety Improvement Act in the U.S. and the Registration, Evaluation, Authorization, and Restriction of Chemicals legislation in the EU demonstrates increasing regulatory and stakeholder concern surrounding the use of harmful or potentially harmful substances in consumer products, including apparel, accessories, and footwear. Finished apparel and footwear products have been found to contain traces of chemicals that have been banned or regulated. Depending on the chemical, the amount present in a product, and the type of exposure that consumers face, specific substances can be carcinogenic, and can disrupt hormone activity in humans and other organisms. Failure to manage this issue may generate additional regulatory oversight and impact a company’s social license to operate. In addition, the presence of harmful chemicals in products can lead to recalls, litigation, and reputational damage. Companies in this industry can work in both the design and manufacturing phases to manage the use of chemicals of concern, develop safe alternatives, and eliminate those that have been banned. Given the industry’s reliance on outsourced manufacturing, this involves proactive partnerships with suppliers. In managing this issue, companies must balance the hazard posed to consumers presented by certain chemicals with the quality of a product and its costs of production.')


st.subheader('This is a map :')

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