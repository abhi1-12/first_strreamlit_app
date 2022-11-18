
import streamlit 
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title("My Parents new Healthy Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("🥗Omega 3 and Blueberry Oatmeal")
streamlit.text("Kale, Spinach and Rocket Smothie")
streamlit.text("🐔Hard Boiled Free Range Egg")
streamlit.text('🥑Avacado Toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#lets put a select list so that they can select the fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#print the dataframe
streamlit.dataframe(fruits_to_show)

#function for getting fruit choice
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
      # write your own comment -what does the next line do? 
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
      # write your own comment - what does this do?
    return fruityvice_normalized

                                       
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
      streamlit.error("please select a fruit to get information")
    else:
      back_from_function=get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
    
except URLError as e:
    streamlit.error()
 

#streamlit.stop()
streamlit.header("The Fruit load list contains : ")
#snowflake related function
def get_fruit_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from public.fruit_load_list")
        return my_cur.fetchall()
#add button
if streamlit.button('Get fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows= get_fruit_list()
    streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding" + new_fruit
 
add_my_fruit=streamlit.text_input("what fruit would you like to add?")
if streamlit.button("Add fruit to list"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function=insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
        
    
#my_cur = my_cnx.cursor()
#streamlit.dataframe(my_data_rows)
#add_my_fruit= streamlit.text_input('What fruit would you like to add?','JackFruit')
#streamlit.write('Thanks for entering ',add_my_fruit)
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")




