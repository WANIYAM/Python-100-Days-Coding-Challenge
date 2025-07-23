# 87.Day 87: Student Marks Input & Grade Calculator (with visualization)
# Input marks for 3-4 subjects.
# Calculate percentage and grade.
# Visualize subject-wise marks using st.bar_chart.

import streamlit as st
import pandas as pd

# --- App Title ---
st.title("🎓 Student Marks & Grade Calculator")

# --- Input ---
st.header("Enter Marks for Each Subject (Out of 100)")
subjects = ["Math", "Science", "English", "History"]
marks = {}

for subject in subjects:
    marks[subject] = st.number_input(f"{subject} Marks", min_value=0, max_value=100, step=1)

# --- Calculate ---
if st.button("Calculate Result"):
    total = sum(marks.values())
    num_subjects = len(subjects)
    percentage = total / num_subjects

    # Grade Calculation
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # --- Display Result ---
    st.subheader("📊 Result")
    st.write(f"**Total Marks:** {total} / {100 * num_subjects}")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")

    # --- Visualization ---
    st.subheader("📈 Marks Visualization")
    df = pd.DataFrame({
        "Subject": list(marks.keys()),
        "Marks": list(marks.values())
    })

    st.bar_chart(df.set_index("Subject"))

