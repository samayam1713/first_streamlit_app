import streamlit 

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & Bluebeery oatmeal')
streamlit.text('🥗 kale, spinach & Rocket Smoothiee')
streamlit.text('🐔 Hot-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read.csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
