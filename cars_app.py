# import the frameworks
import streamlit as st
import pandas as pd
import plotly.express as px

# Import the dataset
car_data = pd.read_csv('vehicles.csv')

# Making the header
st.header("Does it influence the price of your vehicle or not?")
st.subheader("Let's discover the factors that influence the price of your vehicle when selling it by analyzing some online ads data.")


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
title_odometer = st.title('Odometer x Price')
build_odometer = st.write(
    "Discover how much your car's mileage influences when it comes to selling.")
build_dispersion_odometer = st.button('See the chart here of Odometer x Price')

if build_dispersion_odometer:
    st.write('Creating a scatter graph for the car sales ads dataset')
    st.scatter_chart(odometer_price, y='price', x='odometer', color='odometer')

# The Second table (Year x Price)
title_year = st.title('Year x Price')
build_year = st.write(
    "Discover how much your car's year influences when it comes to selling.")
build_bar_year = st.button('See the chart here of Year x Price')

if build_bar_year:
    st.write('Creating a bar graph for the car sales ads dataset')
    st.bar_chart(year_price, x='model_year', y='price', color='price')

# The third table (Condition x Price)

title_condition = st.title('Condition x Price')
build_condition = st.write(
    "Discover how much a car's condition influences when it comes to selling it.")
build_scatter_condition = st.button('See the chart  of Condition x Price')


if build_scatter_condition:
    st.write('Creating a scatter graph for the car sales ads dataset')
    st.scatter_chart(condition_price, y='condition', x='price', color='price')

# The fourth table (Fuel x Price)

title_fuel = st.title('Fuel x Price')
build_fuel = st.write(
    "Discover how much a car's fuel consumption influences the time to sell it.")
build_hist_fuel = st.button('See the chart here of Fuel x Price')


if build_hist_fuel:
    st.write('Creating a histogram graph for the car sales ads dataset')
    fig = px.histogram(fuel_price, x='fuel', y='price', color='fuel')
    st.plotly_chart(fig, use_container_width=True)


# The fifth table (Type x Price)

title_type = st.title("Type of cars x Price")
build_type = st.write(
    'Discover how much the type of car influences the price when selling it')
build_scatter_type = st.button('See the chart here of Type x Price')


if build_scatter_type:
    st.write('Creating a scatter graph for the car sales ads dataset')
    st.scatter_chart(type_price, y='type', x='price', color='type')
