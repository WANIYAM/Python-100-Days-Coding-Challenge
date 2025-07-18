# 82.Day 82: Building First Interactive App
# Create an input form that takes a name and age and displays them using st.text_input and st.number_input.

import streamlit as st

st.title("Day 82: My First Interactive App")

# Input fields
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)

# Display the results
if name and age:
    st.write(f"Hello, **{name}**! You are **{int(age)}** years old.")
