
import streamlit 

streamlit.title("My Parents new Healthy Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("🥗Omega 3 and Blueberry Oatmeal")
streamlit.text("Kale, Spinach and Rocket Smothie")
streamlit.text("🐔Hard Boiled Free Range Egg")
streamlit.text('🥑Avacado Toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#lets put a select list so that they can select the fruit
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#print the dataframe
streamlit.dataframe(my_fruit_list)


