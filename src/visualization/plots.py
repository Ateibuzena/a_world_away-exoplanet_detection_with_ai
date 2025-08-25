import streamlit as st
import plotly.express as px

def plot_light_curve(df):
    if 'time' in df.columns and 'flux' in df.columns:
        fig = px.line(df, x='time', y='flux', title='Curva de luz')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("CSV no tiene columnas 'time' y 'flux'")
