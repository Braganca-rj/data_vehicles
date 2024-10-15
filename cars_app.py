import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')
# Header
st.header("Does it influence the price of your vehicle or not?")
st.subheader("Let's discover the factors that influence the price of your vehicle when selling it by analyzing some online ads data.")

# Changer the background-color
page_bg_color = """<style >
body{background-color:  # f0f0f0;
}</style >"""


st.markdown(page_bg_color, unsafe_allow_html=True)

# Groupings used to calculate the table values.
odometer_price = car_data.groupby(
    'odometer')['price'].value_counts().reset_index()

year_price = car_data.groupby('model_year')[
    'price'].value_counts().reset_index()

condition_price = car_data.groupby(
    'condition')['price'].value_counts().reset_index()

fuel_price = car_data.groupby('fuel')['price'].value_counts().reset_index()

type_price = car_data.groupby('type')['price'].value_counts().reset_index()

# The First table(Odometer x Price)
build_hist = st.write(
    "Discover how much your car's mileage influences its sale.")
build_dispersion_odometer = st.button('Create dispersion')

if build_dispersion_odometer:
    st.write('Creating a histogram for the car sales ads dataset')
    st.scatter_chart(odometer_price, y='price', x='odometer', color='odometer')
