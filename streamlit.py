import streamlit as st
import pandas as pd


st.header("Finding the biggest value of the three given numbers")
st.subheader('User Input Values')
value_1 = st.number_input("Value 1")
value_2 = st.number_input("Value 2")
value_3 = st.number_input("Value 3")

st.subheader("the largest value of the three is")
if (value_1>value_2 and value_1>value_3):
  st.write("Value 1")
elif (value_2>value_1 and value_2>value_3):
  st.write("Value 2")
else:
  st.write("Value 3")