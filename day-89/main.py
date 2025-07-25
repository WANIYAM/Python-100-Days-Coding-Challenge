import streamlit as st
import pandas as pd

# App title
st.title("📊 Data Display App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Check if a file is uploaded
if uploaded_file is not None:
    try:
        # Read the CSV into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Show success message
        st.success("✅ File uploaded successfully!")

        # Display the dataframe
        st.dataframe(df)

    except Exception as e:
        st.error(f"Error reading the file: {e}")
else:
    st.info("Please upload a CSV file to get started.")

