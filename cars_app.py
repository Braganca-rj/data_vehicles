import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')

build_hist = st.checkbox('Create histogram')
build_dispersion = st.checkbox('Create dispersion')


if build_hist:
    st.write('Creating a histogram for the car sales ads dataset')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_dispersion:
    st.write('Creating a histogram for the car sales ads dataset')
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
