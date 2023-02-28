import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Img1.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "movies.csv")

st.title("Dashboard - IMDB Movies Data")

img = image.imread(IMAGE_PATH)
st.image(img, width=700, use_column_width=500)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Year = st.selectbox("Select the year:", df['year'].unique())
Genre = st.selectbox("Select the genre:", df['genre'].unique())
Certificate = st.selectbox("Select the certificate:", df['certificate'].unique())


col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['year'] == Year], x="name", y="rating")
fig_1 = px.histogram(df[df['genre'] == Genre], x="name", y="rating")
fig_1 = px.histogram(df[df['certificate'] == Certificate], x="name", y="rating")


col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['year'] == Year], x="name", y="rating")
fig_2 = px.box(df[df['genre'] == Genre], x="name", y="rating")
fig_2 = px.box(df[df['certificate'] == Certificate], x="name", y="rating")


col2.plotly_chart(fig_2, use_container_width=True)