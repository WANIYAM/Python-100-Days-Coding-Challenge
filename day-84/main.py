# 84.Day 84: Simple Calculator App using Streamlit
# Add two number inputs.
# Let users select operation (+, -, *, /) via st.selectbox.
# Display result on button click.

import streamlit as st

# Title
st.title("🧮 Simple Calculator")

# Number Inputs
num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f")

# Operation selection
operation = st.selectbox("Choose operation", ["+", "-", "*", "/"])

# Calculate on button click
if st.button("Calculate"):
    result = None
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"

        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")
