import streamlit as st

import pandas as pd


def find_largest(num1,num2,num3):
  return max(number1, number2, number3)

st.title('Find the Largest Number')

number1 = st.number_input("Insert first number", value=None, placeholder="Type a number...")
number2 = st.number_input("Insert second number", value=None, placeholder="Type a number...")
number3 = st.number_input("Insert third number", value=None, placeholder="Type a number...")

if st.button('Find Largest'):
  largest = find_largest(number1, number2, number3)
  st.write('The largest number is: ', largest)
