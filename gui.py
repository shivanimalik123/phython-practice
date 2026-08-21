# import tkinter as tk

# window = tk.Tk()
# window.configure(bg="#EAF2F8")
# window.resizable(False, False)
# window.title("Smart Student Performance Analysis System")
# window.geometry("700x700")


# def analyze():
#     name = name_entry.get()
#     roll = roll_entry.get()

#     python_marks = float(python_entry.get())
#     sql_marks = float(sql_entry.get())
#     pandas_marks = float(pandas_entry.get())

#     average = (python_marks + sql_marks + pandas_marks) / 3

#     if average >= 80:
#         performance = "Excellent"
#         grade = "A"
#     elif average >= 60:
#         performance = "Good"
#         grade = "B"
#     elif average >= 40:
#         performance = "Average"
#         grade = "C"
#     else:
#         performance = "Needs Improvement"
#         grade = "D"

#     if python_marks >= sql_marks and python_marks >= pandas_marks:
#         best_subject = "Python"
#     elif sql_marks >= python_marks and sql_marks >= pandas_marks:
#         best_subject = "SQL"
#     else:
#         best_subject = "Pandas"

#     if python_marks <= sql_marks and python_marks <= pandas_marks:
#         weak_subject = "Python"
#     elif sql_marks <= python_marks and sql_marks <= pandas_marks:
#         weak_subject = "SQL"
#     else:
#         weak_subject = "Pandas"

#     if weak_subject == "Python":
#         suggestion = "Practice Python programs regularly."
#     elif weak_subject == "SQL":
#         suggestion = "Practice SQL queries regularly."
#     else:
#         suggestion = "Practice Pandas and data analysis regularly."

#     result = (
#         "STUDENT PERFORMANCE REPORT\n\n"
#         f"Student Name: {name}\n"
#         f"Roll Number: {roll}\n\n"
#         f"Python Marks: {python_marks}\n"
#         f"SQL Marks: {sql_marks}\n"
#         f"Pandas Marks: {pandas_marks}\n\n"
#         f"Average Marks: {round(average, 2)}\n"
#         f"Performance: {performance}\n"
#         f"Grade: {grade}\n"
#         f"Best Subject: {best_subject}\n"
#         f"Need Improvement: {weak_subject}\n"
#         f"Suggestion: {suggestion}"
#     )
#     result_label.config(text=result)

# title = tk.Label(
#     window,
#     text="SMART STUDENT PERFORMANCE ANALYSIS SYSTEM",
#     font=("Arial", 18, "bold")
# )
# title.pack(pady=20)

# details_title = tk.Label(window,text="Student Details",font=("Arial", 14, "bold"))
# details_title.pack(pady=10)

# name_label = tk.Label(window, text="Student Name")
# name_label.pack()

# name_entry = tk.Entry(window, width=35)
# name_entry.pack(pady=5)

# roll_label = tk.Label(window, text="Roll Number")
# roll_label.pack()

# roll_entry = tk.Entry(window, width=35)
# roll_entry.pack(pady=5)

# python_label = tk.Label(window, text="Python Marks")
# python_label.pack()

# python_entry = tk.Entry(window, width=35)
# python_entry.pack(pady=5)

# sql_label = tk.Label(window, text="SQL Marks")
# sql_label.pack()

# sql_entry = tk.Entry(window, width=35)
# sql_entry.pack(pady=5)

# pandas_label = tk.Label(window, text="Pandas Marks")
# pandas_label.pack()

# pandas_entry = tk.Entry(window, width=35)
# pandas_entry.pack(pady=5)

# analyze_button = tk.Button(
#     window,
#     text="Analyze Performance",
#     font=("Arial", 12, "bold"),
#     padx=15,
#     pady=5,
#     command=analyze
# )
# analyze_button.pack(pady=20)

# result_label = tk.Label(
#     window,
#     text="",font=("Arrial", 12),justify="left",relief="groove",padx=15,pady=15)
# result_label.pack(pady=10)
# window.mainloop()
