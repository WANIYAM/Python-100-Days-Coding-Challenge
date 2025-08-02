# 95.Day 95: Flashcards App (for learning)
# Input Q&A pairs.
# Show random flashcards on button click.

import streamlit as st
import random

st.set_page_config(page_title="Flashcards App", layout="centered")

st.title("📚 Flashcards App")

# Session state to store flashcards
if "flashcards" not in st.session_state:
    st.session_state.flashcards = []

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

if "current_card" not in st.session_state:
    st.session_state.current_card = None

# Form to add flashcards
with st.form("add_flashcard"):
    st.subheader("➕ Add Flashcard")
    question = st.text_input("Question")
    answer = st.text_input("Answer")
    submitted = st.form_submit_button("Add")
    if submitted:
        if question and answer:
            st.session_state.flashcards.append({"question": question, "answer": answer})
            st.success("Flashcard added!")
        else:
            st.error("Both fields are required.")

st.divider()

# Show flashcard
if st.session_state.flashcards:
    if st.button("🎲 Show Random Flashcard"):
        st.session_state.current_card = random.choice(st.session_state.flashcards)
        st.session_state.show_answer = False

    if st.session_state.current_card:
        card = st.session_state.current_card
        if st.session_state.show_answer:
            st.subheader("📝 Answer:")
            st.info(card['answer'])
        else:
            st.subheader("❓ Question:")
            st.info(card['question'])

        if st.button("🔁 Flip"):
            st.session_state.show_answer = not st.session_state.show_answer
else:
    st.warning("No flashcards yet. Add some above!")

