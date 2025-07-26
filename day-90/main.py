# 90.Day 90: Survey Form (Interactive Form)
# Take user feedback on 4-5 questions (using radio, checkbox, text input).
# Display summary of inputs.

import tkinter as tk
from tkinter import messagebox

def submit_form():
    summary = []

    # Q1: Experience
    summary.append(f"1. Overall Experience: {experience_var.get()}")

    # Q2: Features Liked
    liked_features = []
    if feature1_var.get():
        liked_features.append("User Interface")
    if feature2_var.get():
        liked_features.append("Performance")
    if feature3_var.get():
        liked_features.append("Features")
    if feature4_var.get():
        liked_features.append("Support")
    summary.append("2. Features Liked: " + ", ".join(liked_features) if liked_features else "2. Features Liked: None")

    # Q3: Would Recommend
    summary.append(f"3. Recommend to Others: {recommend_var.get()}")

    # Q4: Suggestions
    summary.append("4. Suggestions/Comments: " + suggestions_entry.get("1.0", tk.END).strip())

    # Display summary in messagebox
    messagebox.showinfo("Survey Summary", "\n\n".join(summary))

# Main window
root = tk.Tk()
root.title("User Feedback Survey Form")
root.geometry("500x500")
root.resizable(False, False)

# --- Question 1 ---
tk.Label(root, text="1. How would you rate your overall experience?", anchor='w').pack(fill='x')
experience_var = tk.StringVar(value="Good")
tk.Radiobutton(root, text="Excellent", variable=experience_var, value="Excellent").pack(anchor='w')
tk.Radiobutton(root, text="Good", variable=experience_var, value="Good").pack(anchor='w')
tk.Radiobutton(root, text="Average", variable=experience_var, value="Average").pack(anchor='w')
tk.Radiobutton(root, text="Poor", variable=experience_var, value="Poor").pack(anchor='w')

# --- Question 2 ---
tk.Label(root, text="\n2. What features did you like? (Select all that apply)", anchor='w').pack(fill='x')
feature1_var = tk.BooleanVar()
feature2_var = tk.BooleanVar()
feature3_var = tk.BooleanVar()
feature4_var = tk.BooleanVar()
tk.Checkbutton(root, text="User Interface", variable=feature1_var).pack(anchor='w')
tk.Checkbutton(root, text="Performance", variable=feature2_var).pack(anchor='w')
tk.Checkbutton(root, text="Features", variable=feature3_var).pack(anchor='w')
tk.Checkbutton(root, text="Support", variable=feature4_var).pack(anchor='w')

# --- Question 3 ---
tk.Label(root, text="\n3. Would you recommend this to others?", anchor='w').pack(fill='x')
recommend_var = tk.StringVar(value="Yes")
tk.Radiobutton(root, text="Yes", variable=recommend_var, value="Yes").pack(anchor='w')
tk.Radiobutton(root, text="No", variable=recommend_var, value="No").pack(anchor='w')

# --- Question 4 ---
tk.Label(root, text="\n4. Any suggestions or comments?", anchor='w').pack(fill='x')
suggestions_entry = tk.Text(root, height=4, width=60)
suggestions_entry.pack(pady=5)

# --- Submit Button ---
tk.Button(root, text="Submit Feedback", command=submit_form, bg="green", fg="white", width=20).pack(pady=20)

# Start GUI loop
root.mainloop()
