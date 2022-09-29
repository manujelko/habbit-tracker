from flask import Flask, render_template, request

app = Flask(__name__)
habits = []

@app.route("/")
def index():
    return render_template("index.html.j2", title="Habit Tracker - Home", habits=habits)


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habits.append(request.form.get("habit"))
    return render_template("add_habit.html.j2", title="Habit Tracker - Add Habit")
