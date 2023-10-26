import streamlit
streamlit.title(' 🥣My parents New healthy diner')
streamlit.header(' 🥗Breakfast menu')
streamlit.text('  🐔 omega 3 & blueberry Oatmeal')
streamlit.text(' 🥑 kale, Spinach & rocket smoothie')
streamlit.text(' 🍞 hard-boiled free-range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
