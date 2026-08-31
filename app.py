"""
Smart Student Performance Analysis System
Professional web dashboard - Flask backend.

Run:
    python app.py
Then open http://127.0.0.1:5000
Demo credentials: username = admin  (or admin@student.com)  /  password = admin123
"""
import io
import base64
import os
from datetime import timedelta

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from flask import (Flask, render_template, request, jsonify, session,
                   redirect, url_for)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")
app.permanent_session_lifetime = timedelta(days=30)

# Demo credential store (no database needed for the project).
USERS = {"admin": "admin123", "admin@student.com": "admin123"}

# In-memory student records store (no database for this project).
RECORDS = []


# ---------------- ANALYSIS LOGIC (kept from original project) ----------------
def analyze_student(name, roll, course, attendance, python, sql, pandas):
    """Core analysis. Returns a dict of computed results. Logic unchanged."""
    average = (python + sql + pandas) / 3

    if average >= 80:
        performance = "Excellent"
        grade = "A"
    elif average >= 60:
        performance = "Good"
        grade = "B"
    elif average >= 40:
        performance = "Average"
        grade = "C"
    else:
        performance = "Needs Improvement"
        grade = "D"

    subjects = {"Python": python, "SQL": sql, "Pandas": pandas}
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
        "name": name, "roll": roll, "course": course,
        "attendance": attendance, "attendance_val": float(attendance) if attendance else None,
        "python": python, "sql": sql, "pandas": pandas,
        "subjects": subjects, "average": round(average, 2), "grade": grade,
        "performance": performance, "best": best, "weak": weak,
        "suggestion": suggestion, "remark": remark,
    }


def build_chart(python, sql, pandas):
    """Return a base64 PNG bar chart of the three subjects."""
    fig, ax = plt.subplots(figsize=(6.2, 3.4), dpi=110)
    labels = ["Python", "SQL", "Pandas"]
    values = [python, sql, pandas]
    colors = ["#6366f1", "#22c58e", "#3b82f6"]
    bars = ax.bar(labels, values, color=colors, edgecolor="white",
                  linewidth=1.6, width=0.55)
    ax.set_ylim(0, 110)
    ax.set_ylabel("Marks")
    ax.set_title("Subject-wise Performance")
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color("#CBD5E1")
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 3, f"{int(v)}",
                ha="center", va="bottom", fontweight="bold", fontsize=10)
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


def build_report_text(data):
    """Build the human-readable report string (kept from original format)."""
    sep = "=" * 52
    lines = [
        sep,
        "       SMART STUDENT PERFORMANCE REPORT",
        sep,
        f"Date          : {data.get('date','')}",
        f"Student Name  : {data['name']}",
        f"Roll Number   : {data['roll']}",
        f"Class/Course  : {data['course']}",
        f"Attendance    : {data['attendance']}%",
        "-" * 52,
        f"Python Marks  : {int(data['python'])}",
        f"SQL Marks     : {int(data['sql'])}",
        f"Pandas Marks  : {int(data['pandas'])}",
        "-" * 52,
        f"Average Marks : {data['average']}",
        f"Grade         : {data['grade']}",
        f"Performance   : {data['performance']}",
        f"Best Subject  : {data['best']}",
        f"Weak Subject  : {data['weak']}",
        f"Suggestion    : {data['suggestion']}",
        f"Overall Remark: {data['remark']}",
        sep,
    ]
    return "\n".join(lines)


def parse_inputs(payload):
    """Validate incoming JSON payload. Returns (data, error_str)."""
    name = str(payload.get("name", "")).strip()
    roll = str(payload.get("roll", "")).strip()
    course = str(payload.get("course", "")).strip()
    attendance = str(payload.get("attendance", "")).strip()
    try:
        python = float(payload.get("python", ""))
        sql = float(payload.get("sql", ""))
        pandas = float(payload.get("pandas", ""))
    except (ValueError, TypeError):
        return None, "Please enter valid numeric marks for all subjects."
    if not name or not roll:
        return None, "Please enter student name and roll number."
    if not (0 <= python <= 100 and 0 <= sql <= 100 and 0 <= pandas <= 100):
        return None, "Marks should be between 0 and 100."
    if attendance:
        try:
            av = float(attendance)
            if not (0 <= av <= 100):
                return None, "Attendance must be between 0 and 100."
        except ValueError:
            return None, "Attendance must be a valid number."
    return (name, roll, course, attendance, python, sql, pandas), None


# ---------------- ROUTES ----------------
@app.route("/")
def home():
    if session.get("user"):
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = str(data.get("username", "")).strip()
    password = str(data.get("password", ""))
    remember = data.get("remember", False)
    if USERS.get(username) == password:
        session.permanent = True
        if not remember:
            session.permanent = False
        session["user"] = username
        return jsonify({"ok": True})
    return jsonify({"ok": False, "error": "Invalid username or password."}), 401


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route("/dashboard")
def dashboard():
    if not session.get("user"):
        return redirect(url_for("home"))
    return render_template("dashboard.html", user=session.get("user"))


@app.route("/analyze", methods=["POST"])
def analyze():
    payload = request.get_json(silent=True) or {}
    parsed, err = parse_inputs(payload)
    if err:
        return jsonify({"ok": False, "error": err})
    name, roll, course, attendance, python, sql, pandas = parsed
    data = analyze_student(name, roll, course, attendance, python, sql, pandas)
    data["chart"] = build_chart(python, sql, pandas)
    data["date"] = ""
    return jsonify({"ok": True, **data})


@app.route("/report", methods=["POST"])
def report():
    from datetime import datetime
    payload = request.get_json(silent=True) or {}
    parsed, err = parse_inputs(payload)
    if err:
        return jsonify({"ok": False, "error": err})
    name, roll, course, attendance, python, sql, pandas = parsed
    data = analyze_student(name, roll, course, attendance, python, sql, pandas)
    data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = build_report_text(data)
    filename = f"student_report_{''.join(c for c in roll if c.isalnum()) or 'report'}.txt"
    return jsonify({"ok": True, "report": text, "filename": filename})


@app.route("/api/records", methods=["GET", "POST"])
def records():
    if request.method == "GET":
        return jsonify({"ok": True, "records": RECORDS})
    payload = request.get_json(silent=True) or {}
    parsed, err = parse_inputs(payload)
    if err:
        return jsonify({"ok": False, "error": err})
    name, roll, course, attendance, python, sql, pandas = parsed
    from datetime import datetime
    data = analyze_student(name, roll, course, attendance, python, sql, pandas)
    record = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": data["name"], "roll": data["roll"], "course": data["course"],
        "attendance": data["attendance"], "python": int(data["python"]),
        "sql": int(data["sql"]), "pandas": int(data["pandas"]),
        "average": data["average"], "grade": data["grade"],
        "performance": data["performance"], "best": data["best"], "weak": data["weak"],
    }
    RECORDS.append(record)
    return jsonify({"ok": True, "record": record, "count": len(RECORDS)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
