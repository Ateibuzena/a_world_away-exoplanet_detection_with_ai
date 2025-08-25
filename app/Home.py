import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.data.loaders import load_sample_dataset
from src.visualization.plots import plot_light_curve

st.set_page_config(page_title="A World Away", layout="wide")
st.title("A World Away: Hunting for Exoplanets with AI")

uploaded_file = st.file_uploader("Cargar dataset CSV", type=["csv"])
if uploaded_file:
    df = load_sample_dataset(uploaded_file)
    st.write(df.head())
    plot_light_curve(df)
else:
    st.info("Sube un CSV con curvas de luz para visualizar")
