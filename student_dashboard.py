import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# ================= COLORS =================
BG = "#F5F6FA"
SIDEBAR_BG = "#2D3748"
SIDEBAR_ACTIVE = "#4A7C8C"
SIDEBAR_TEXT = "#E2E8F0"
HEADER_BG = "#2C3E50"
CARD_BG = "#FFFFFF"
BORDER = "#E3E8EF"
PRIMARY = "#4A7C8C"
RESET = "#E76F51"
REPORT = "#0984E3"
TEXT = "#2C3E50"
MUTED = "#7180AB"


# ================= WINDOW =================
window = tk.Tk()
window.title("Smart Student Performance Analysis System")
window.geometry("1100x720")
window.minsize(900, 640)
window.configure(bg=BG)


FONT = ("Segoe UI", 10)
BOLD = ("Segoe UI", 11, "bold")
TITLE = ("Segoe UI", 15, "bold")


# ================= VARIABLES =================
name_var = tk.StringVar()
roll_var = tk.StringVar()
course_var = tk.StringVar()
attendance_var = tk.StringVar()

python_var = tk.StringVar()
sql_var = tk.StringVar()
pandas_var = tk.StringVar()

avg_var = tk.StringVar(value="—")
grade_var = tk.StringVar(value="—")
best_var = tk.StringVar(value="—")
att_result_var = tk.StringVar(value="—")

overview_var = tk.StringVar(
    value="Enter student details and click Analyze Performance."
)

strong_var = tk.StringVar(value="—")
weak_var = tk.StringVar(value="—")
recommendation_var = tk.StringVar(value="No recommendations yet.")


# ================= HEADER =================
header = tk.Frame(window, bg=HEADER_BG, height=62)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="Smart Student Performance Analysis System",
    font=TITLE,
    bg=HEADER_BG,
    fg="white"
).pack(side="left", padx=22)

tk.Label(
    header,
    text="📊 Dashboard",
    font=BOLD,
    bg=HEADER_BG,
    fg="#B2EBF2"
).pack(side="right", padx=22)


# ================= MAIN =================
main = tk.Frame(window, bg=BG)
main.pack(fill="both", expand=True, padx=18, pady=15)

main.grid_columnconfigure(1, weight=1)
main.grid_rowconfigure(0, weight=1)


# ================= SIDEBAR =================
sidebar = tk.Frame(main, bg=SIDEBAR_BG, width=210)
sidebar.grid(row=0, column=0, sticky="ns", padx=(0, 14))
sidebar.grid_propagate(False)

tk.Label(
    sidebar,
    text="Menu",
    font=("Segoe UI", 12, "bold"),
    bg=SIDEBAR_BG,
    fg="#B2EBF2",
    anchor="w",
    padx=20,
    pady=12
).pack(fill="x")


def sidebar_button(text):
    return tk.Button(
        sidebar,
        text=text,
        font=BOLD,
        bg=SIDEBAR_BG,
        fg=SIDEBAR_TEXT,
        activebackground=SIDEBAR_ACTIVE,
        activeforeground="white",
        relief="flat",
        anchor="w",
        padx=18,
        pady=10
    )


dashboard_btn = sidebar_button("🏠 Dashboard")
analysis_btn = sidebar_button("👤 Student Analysis")
report_menu_btn = sidebar_button("📄 Reports")

dashboard_btn.pack(fill="x", padx=6, pady=3)
analysis_btn.pack(fill="x", padx=6, pady=3)
report_menu_btn.pack(fill="x", padx=6, pady=3)

dashboard_btn.config(bg=SIDEBAR_ACTIVE, fg="white")


# ================= SCROLLABLE CONTENT =================
content_area = tk.Frame(main, bg=BG)
content_area.grid(row=0, column=1, sticky="nsew")

content_area.grid_rowconfigure(0, weight=1)
content_area.grid_columnconfigure(0, weight=1)

canvas = tk.Canvas(
    content_area,
    bg=BG,
    highlightthickness=0
)
canvas.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(
    content_area,
    orient="vertical",
    command=canvas.yview
)
scrollbar.grid(row=0, column=1, sticky="ns")

canvas.configure(yscrollcommand=scrollbar.set)

content = tk.Frame(canvas, bg=BG)

canvas_window = canvas.create_window(
    (0, 0),
    window=content,
    anchor="nw"
)


def update_scroll(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))


def resize_content(event):
    canvas.itemconfig(canvas_window, width=event.width)


content.bind("<Configure>", update_scroll)
canvas.bind("<Configure>", resize_content)


# ================= INPUT CARD =================
input_box = tk.Frame(
    content,
    bg=CARD_BG,
    relief="solid",
    bd=1,
    highlightbackground=BORDER,
    highlightthickness=1
)
input_box.pack(fill="x", pady=(0, 14))

tk.Label(
    input_box,
    text="Student Information",
    font=("Segoe UI", 13, "bold"),
    bg=CARD_BG,
    fg=TEXT
).grid(
    row=0,
    column=0,
    columnspan=6,
    sticky="w",
    padx=15,
    pady=12
)


def make_entry(row, col, label, variable):
    tk.Label(
        input_box,
        text=label,
        font=BOLD,
        bg=CARD_BG,
        fg=PRIMARY
    ).grid(
        row=row,
        column=col,
        sticky="e",
        padx=6,
        pady=8
    )

    entry = tk.Entry(
        input_box,
        textvariable=variable,
        width=14,
        font=FONT,
        relief="solid",
        bd=1
    )
    entry.grid(
        row=row,
        column=col + 1,
        sticky="w",
        padx=6,
        pady=8
    )

    return entry


name_entry = make_entry(
    1, 0, "Student Name", name_var
)

roll_entry = make_entry(
    1, 2, "Roll No", roll_var
)

course_entry = make_entry(
    2, 0, "Class/Course", course_var
)

attendance_entry = make_entry(
    2, 2, "Attendance (%)", attendance_var
)

python_entry = make_entry(
    3, 0, "Python Marks", python_var
)

sql_entry = make_entry(
    3, 2, "SQL Marks", sql_var
)

pandas_entry = make_entry(
    4, 0, "Pandas Marks", pandas_var
)


# ================= BUTTONS =================
btn_row = tk.Frame(content, bg=BG)
btn_row.pack(fill="x", pady=(0, 14))


# ================= DASHBOARD FUNCTIONS =================
def get_student_data():

    name = name_var.get().strip()
    roll = roll_var.get().strip()
    course = course_var.get().strip()
    attendance = attendance_var.get().strip()

    try:
        python = float(python_var.get())
        sql = float(sql_var.get())
        pandas = float(pandas_var.get())
    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numeric marks for Python, SQL and Pandas."
        )
        return None

    if not name or not roll:
        messagebox.showwarning(
            "Missing Information",
            "Please enter Student Name and Roll No."
        )
        return None

    if not (0 <= python <= 100):
        messagebox.showerror("Error", "Python marks must be 0-100.")
        return None

    if not (0 <= sql <= 100):
        messagebox.showerror("Error", "SQL marks must be 0-100.")
        return None

    if not (0 <= pandas <= 100):
        messagebox.showerror("Error", "Pandas marks must be 0-100.")
        return None

    average = (python + sql + pandas) / 3

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

    subjects = {
        "Python": python,
        "SQL": sql,
        "Pandas": pandas
    }

    best = max(subjects, key=subjects.get)
    weak = min(subjects, key=subjects.get)

    if weak == "Python":
        suggestion = "Practice Python programs regularly."
    elif weak == "SQL":
        suggestion = "Practice SQL queries regularly."
    else:
        suggestion = "Practice Pandas and data analysis regularly."

    if average >= 80:
        remark = "Excellent performance. Keep it up!"
    elif average >= 60:
        remark = "Good performance. Keep practicing."
    elif average >= 40:
        remark = "Average performance. More practice is needed."
    else:
        remark = "Needs improvement. Focus on your weak subject."

    return {
        "name": name,
        "roll": roll,
        "course": course,
        "attendance": attendance,
        "python": python,
        "sql": sql,
        "pandas": pandas,
        "average": average,
        "grade": grade,
        "performance": performance,
        "subjects": subjects,
        "best": best,
        "weak": weak,
        "suggestion": suggestion,
        "remark": remark
    }


# ================= CHART =================
chart_holder = tk.Frame(
    content,
    bg=CARD_BG,
    relief="solid",
    bd=1,
    highlightbackground=BORDER,
    highlightthickness=1,
    height=320
)
chart_holder.pack(fill="x", pady=(0, 14))
chart_holder.pack_propagate(False)


def update_chart(data):

    for widget in chart_holder.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(
        figsize=(7, 3.2),
        dpi=90
    )

    labels = ["Python", "SQL", "Pandas"]

    values = [
        data["python"],
        data["sql"],
        data["pandas"]
    ]

    bars = ax.bar(
        labels,
        values,
        width=0.55
    )

    ax.set_ylim(0, 110)
    ax.set_ylabel("Marks")
    ax.set_title(
        "Subject-wise Performance",
        fontsize=13,
        fontweight="bold"
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.35
    )

    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 3,
            str(int(value)),
            ha="center",
            va="bottom",
            fontweight="bold"
        )

    fig.tight_layout()

    chart = FigureCanvasTkAgg(
        fig,
        chart_holder
    )

    chart.draw()

    chart.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ================= ANALYZE =================
def analyze():

    data = get_student_data()

    if not data:
        return

    avg_var.set(
        f"{data['average']:.2f}"
    )

    grade_var.set(
        data["grade"]
    )

    best_var.set(
        data["best"]
    )

    if data["attendance"]:
        att_result_var.set(
            f"{data['attendance']}%"
        )
    else:
        att_result_var.set("—")

    overview_var.set(
        f"Performance : {data['performance']}\n"
        f"Average     : {data['average']:.2f} / 100\n"
        f"Grade       : {data['grade']}\n"
        f"Best Subject: {data['best']}\n"
        f"Weak Subject: {data['weak']}"
    )

    strong_var.set(
        f"{data['best']}\n"
        f"{int(data['subjects'][data['best']])} / 100"
    )

    weak_var.set(
        f"{data['weak']}\n"
        f"{int(data['subjects'][data['weak']])} / 100"
    )

    recommendation_var.set(
        f"Weakest Subject: {data['weak']}\n"
        f"Recommendation: {data['suggestion']}\n\n"
        f"{data['remark']}"
    )

    student_info.config(
        text=(
            f"{data['name']}  |  "
            f"Roll No: {data['roll']}  |  "
            f"Course: {data['course']}  |  "
            f"Attendance: {data['attendance']}%"
        )
    )

    update_chart(data)


# ================= RESET =================
def reset_form():

    for variable in (
        name_var,
        roll_var,
        course_var,
        attendance_var,
        python_var,
        sql_var,
        pandas_var
    ):
        variable.set("")

    avg_var.set("—")
    grade_var.set("—")
    best_var.set("—")
    att_result_var.set("—")

    overview_var.set(
        "Enter student details and click Analyze Performance."
    )

    strong_var.set("—")
    weak_var.set("—")

    recommendation_var.set(
        "No recommendations yet."
    )

    student_info.config(
        text="Enter student details and click Analyze Performance."
    )

    for widget in chart_holder.winfo_children():
        widget.destroy()


# ================= REPORT =================
def generate_report():

    data = get_student_data()

    if not data:
        return

    report = f"""
SMART STUDENT PERFORMANCE REPORT
========================================

Date          : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Student Name  : {data["name"]}
Roll Number   : {data["roll"]}
Class/Course  : {data["course"]}
Attendance    : {data["attendance"]}%

----------------------------------------
Python Marks  : {int(data["python"])}
SQL Marks     : {int(data["sql"])}
Pandas Marks  : {int(data["pandas"])}

----------------------------------------
Average Marks : {data["average"]:.2f}
Grade         : {data["grade"]}
Performance   : {data["performance"]}
Best Subject  : {data["best"]}
Weak Subject  : {data["weak"]}

Suggestion    : {data["suggestion"]}

Overall Remark:
{data["remark"]}

========================================
"""

    filename = f"student_report_{data['roll']}.txt"

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

    messagebox.showinfo(
        "Report Generated",
        f"Report saved as:\n{filename}"
    )


# ================= BUTTONS =================
tk.Button(
    btn_row,
    text="Analyze Performance",
    font=BOLD,
    bg=PRIMARY,
    fg="white",
    relief="flat",
    padx=18,
    pady=8,
    command=analyze
).pack(
    side="left",
    padx=(0, 10)
)

tk.Button(
    btn_row,
    text="Reset / Clear",
    font=BOLD,
    bg=RESET,
    fg="white",
    relief="flat",
    padx=18,
    pady=8,
    command=reset_form
).pack(
    side="left",
    padx=(0, 10)
)

tk.Button(
    btn_row,
    text="Generate Report",
    font=BOLD,
    bg=REPORT,
    fg="white",
    relief="flat",
    padx=18,
    pady=8,
    command=generate_report
).pack(
    side="left"
)


# ================= DASHBOARD CARDS =================
cards = tk.Frame(content, bg=BG)
cards.pack(fill="x", pady=(0, 14))

cards.grid_columnconfigure(
    (0, 1, 2, 3),
    weight=1
)


def card(parent, title, variable):

    frame = tk.Frame(
        parent,
        bg=CARD_BG,
        relief="solid",
        bd=1,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    tk.Label(
        frame,
        text=title,
        font=BOLD,
        bg=CARD_BG,
        fg=MUTED
    ).pack(
        anchor="w",
        padx=15,
        pady=(14, 4)
    )

    tk.Label(
        frame,
        textvariable=variable,
        font=("Segoe UI", 23, "bold"),
        bg=CARD_BG,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=15,
        pady=(0, 14)
    )

    return frame


card(cards, "Average Marks", avg_var).grid(
    row=0, column=0, sticky="nsew", padx=5
)

card(cards, "Grade", grade_var).grid(
    row=0, column=1, sticky="nsew", padx=5
)

card(cards, "Best Subject", best_var).grid(
    row=0, column=2, sticky="nsew", padx=5
)

card(cards, "Attendance", att_result_var).grid(
    row=0, column=3, sticky="nsew", padx=5
)


# ================= OVERVIEW =================
overview_card = tk.LabelFrame(
    content,
    text="Performance Overview",
    font=BOLD,
    fg=PRIMARY,
    bg=CARD_BG,
    padx=15,
    pady=12
)
overview_card.pack(
    fill="x",
    pady=(0, 14)
)

tk.Label(
    overview_card,
    textvariable=overview_var,
    font=FONT,
    bg=CARD_BG,
    fg=TEXT,
    justify="left"
).pack(
    anchor="w"
)


# ================= STRONG / WEAK =================
subject_row = tk.Frame(content, bg=BG)
subject_row.pack(fill="x", pady=(0, 14))

subject_row.grid_columnconfigure(
    (0, 1),
    weight=1
)

strong = tk.LabelFrame(
    subject_row,
    text="Strong Subject",
    font=BOLD,
    fg="#00B894",
    bg=CARD_BG,
    padx=15,
    pady=12
)
strong.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=(0, 7)
)

tk.Label(
    strong,
    textvariable=strong_var,
    font=("Segoe UI", 13, "bold"),
    bg=CARD_BG,
    fg=TEXT
).pack(pady=10)


weak = tk.LabelFrame(
    subject_row,
    text="Needs Improvement",
    font=BOLD,
    fg=RESET,
    bg=CARD_BG,
    padx=15,
    pady=12
)
weak.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=(7, 0)
)

tk.Label(
    weak,
    textvariable=weak_var,
    font=("Segoe UI", 13, "bold"),
    bg=CARD_BG,
    fg=TEXT
).pack(pady=10)


# ================= RECOMMENDATION =================
recommendation = tk.LabelFrame(
    content,
    text="Smart Recommendation",
    font=BOLD,
    fg=PRIMARY,
    bg=CARD_BG,
    padx=15,
    pady=12
)
recommendation.pack(
    fill="x",
    pady=(0, 14)
)

tk.Label(
    recommendation,
    textvariable=recommendation_var,
    font=FONT,
    bg=CARD_BG,
    fg=TEXT,
    justify="left",
    wraplength=900
).pack(
    anchor="w"
)


# ================= STUDENT INFO =================
student_info = tk.Label(
    content,
    text="Enter student details and click Analyze Performance.",
    font=FONT,
    bg=BG,
    fg=MUTED,
    anchor="w"
)
student_info.pack(
    fill="x",
    pady=(0, 10)
)


# ================= SIDEBAR COMMANDS =================
def scroll_top():
    canvas.yview_moveto(0)


def focus_analysis():
    scroll_top()
    name_entry.focus()


dashboard_btn.config(
    command=scroll_top
)

analysis_btn.config(
    command=focus_analysis
)

report_menu_btn.config(
    command=generate_report
)


# ================= START =================
name_entry.focus()

window.mainloop()