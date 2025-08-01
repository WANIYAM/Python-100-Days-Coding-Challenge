# 94.Day 94: Countdown Timer App (Interactive)
# Input minutes/seconds.
# Show live countdown timer using time.sleep and st.empty.

import streamlit as st
import time

st.title("⏳ Countdown Timer App")

# --- User input ---
col1, col2 = st.columns(2)
with col1:
    minutes = st.number_input("Minutes", min_value=0, max_value=60, value=0, step=1)
with col2:
    seconds = st.number_input("Seconds", min_value=0, max_value=59, value=10, step=1)

if st.button("Start Countdown"):
    total_seconds = int(minutes * 60 + seconds)
    if total_seconds == 0:
        st.warning("Please enter a valid time.")
    else:
        placeholder = st.empty()
        for i in range(total_seconds, -1, -1):
            mins, secs = divmod(i, 60)
            placeholder.markdown(f"## ⏱️ {mins:02d}:{secs:02d}")
            time.sleep(1)
        placeholder.markdown("## ✅ Time's up!")
