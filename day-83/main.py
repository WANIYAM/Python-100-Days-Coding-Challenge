import streamlit as st

# Set page title
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

# Title and description
st.title("⚖️ BMI Calculator")
st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

# Input fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height_cm = st.number_input("Enter your height (cm)", min_value=1.0, format="%.2f")

# BMI Calculation
if st.button("Calculate BMI"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    
    # Determine category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # Display result
    st.success(f"Your BMI is **{bmi:.2f}** – {category}")
