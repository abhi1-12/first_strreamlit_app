
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
my_fruit_list = my_fruit_list.set_index('Fruit')

#lets put a select list so that they can select the fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#print the dataframe
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
#added a text entry box
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit load list contains : ")
streamlit.dataframe(my_data_row)



