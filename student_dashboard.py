import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# ---------------- WINDOW ----------------

window = tk.Tk()
window.title("Smart Student Performance Analysis System")
window.geometry("900x650")
window.configure(bg="#F5f3ff")


# ---------------- ANALYZE ----------------

def analyze():

    try:
        name = name_entry.get()
        roll = roll_entry.get()

        python = float(python_entry.get())
        sql = float(sql_entry.get())
        pandas = float(pandas_entry.get())

        if not name or not roll:
            messagebox.showwarning(
                "Missing Information",
                "Please enter name and roll number."
            )
            return

        if not (0 <= python <= 100 and
                0 <= sql <= 100 and
                0 <= pandas <= 100):

            messagebox.showerror(
                "Invalid Marks",
                "Marks should be between 0 and 100."
            )
            return

        # Average
        average = (python + sql + pandas) / 3

        # Grade
        if average >= 80:
            grade = "A"
            performance = "Excellent"

        elif average >= 60:
            grade = "B"
            performance = "Good"

        elif average >= 40:
            grade = "C"
            performance = "Average"

        else:
            grade = "D"
            performance = "Needs Improvement"

        # Subjects
        subjects = {
            "Python": python,
            "SQL": sql,
            "Pandas": pandas
        }

        best = max(subjects, key=subjects.get)
        weak = min(subjects, key=subjects.get)

        # Result
        result.config(
            text=f"{name}  |  Roll No: {roll}\n\n"
                 f"Average: {average:.2f}     "
                 f"Grade: {grade}\n"
                 f"Performance: {performance}\n"
                 f"Best Subject: {best}\n"
                 f"Needs Improvement: {weak}"
        )

        suggestion.config(
            text=f"💡 Suggestion: Practice {weak} regularly."
        )

        # ---------------- GRAPH ----------------

        for widget in graph.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(
            figsize=(5, 3)
        )

        ax.bar(
            ["Python", "SQL", "Pandas"],
            [python, sql, pandas]
        )

        ax.set_ylim(0, 100)
        ax.set_ylabel("Marks")
        ax.set_title("Subject-wise Performance")

        # Marks on bars
        values = [python, sql, pandas]

        for i, value in enumerate(values):
            ax.text(
                i,
                value + 2,
                str(int(value)),
                ha="center",
                fontweight="bold"
            )

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(
            fig,
            graph
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid marks."
        )


# ---------------- TITLE ----------------

tk.Label(
    window,
    text="SMART STUDENT PERFORMANCE ANALYSIS SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#4A7C8C",
    fg="white",
    pady=15
).pack(fill="x")


# ---------------- INPUT BOX ----------------

input_box = tk.Frame(
    window,
    bg="white",
    padx=20,
    pady=15,
    relief="groove",
    bd=2
)

input_box.pack(
    fill="x",
    padx=25,
    pady=15
)


# Name

tk.Label(
    input_box,
    text="Student Name",
    bg="white",
    fg="#4834D4",
    font=("Arial", 10, "bold")
).grid(row=0, column=0)

name_entry = tk.Entry(
    input_box,
    width=18
)

name_entry.grid(
    row=0,
    column=1,
    padx=10
)


# Roll Number

tk.Label(
    input_box,
    text="Roll No",
    bg="white",
    fg="#4834D4",
    font=("Arial", 10, "bold")
).grid(row=0, column=2)

roll_entry = tk.Entry(
    input_box,
    width=15
)

roll_entry.grid(
    row=0,
    column=3,
    padx=10
)


# Python

tk.Label(
    input_box,
    text="Python",
    bg="white",
    fg="#E84393",
    font=("Arial", 10, "bold")
).grid(row=1, column=0, pady=12)

python_entry = tk.Entry(
    input_box,
    width=15
)

python_entry.grid(
    row=1,
    column=1
)


# SQL

tk.Label(
    input_box,
    text="SQL",
    bg="white",
    fg="#00B894",
    font=("Arial", 10, "bold")
).grid(row=1, column=2)

sql_entry = tk.Entry(
    input_box,
    width=15
)

sql_entry.grid(
    row=1,
    column=3
)


# Pandas

tk.Label(
    input_box,
    text="Pandas",
    bg="white",
    fg="#0984E3",
    font=("Arial", 10, "bold")
).grid(row=1, column=4)

pandas_entry = tk.Entry(
    input_box,
    width=15
)

pandas_entry.grid(
    row=1,
    column=5
)


# ---------------- BUTTON ----------------

tk.Button(
    window,
    text="Analyze Performance",
    font=("Arial", 12, "bold"),
    bg="#4A7C8C",
    fg="white",
    activebackground="#3F6D7A",
    activeforeground="white",
    padx=20,
    pady=8,
    command=analyze
).pack(pady=5)


# ---------------- RESULT ----------------

result = tk.Label(
    window,
    text="Enter student details and marks",
    font=("Arial", 12, "bold"),
    bg="#DFF9FB",
    fg="#2C3E50",
    padx=15,
    pady=10,
    justify="left"
)

result.pack(
    padx=25,
    pady=10,
    fill="x"
)


# ---------------- SUGGESTION ----------------

suggestion = tk.Label(
    window,
    text="",
    font=("Arial", 11, "bold"),
    bg="#FFF3CD",
    fg="#856404",
    pady=8
)

suggestion.pack(
    padx=25,
    fill="x"
)


# ---------------- GRAPH ----------------

graph = tk.Frame(
    window,
    bg="white",
    relief="groove",
    bd=2
)

graph.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=12
)


# ---------------- START ----------------

window.mainloop()