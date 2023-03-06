from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
app.debug = True
@app.route('/', methods = ["GET","POST"])
def index():
    data_path = "/home/samurei/mysite/static/data/visits.csv"
    data = pd.read_csv(data_path, index_col="Page")
    visitor_count = data.loc["index.html"].values[0]

    deep_work_count = data.loc["deep_work.html"].values[0]
    how_to_win_friends_count = data.loc["how_to_win_friends.html"].values[0]
    cant_hurt_me_count = data.loc["cant_hurt_me.html"].values[0]
    atomic_habits_count = data.loc["atomic_habits.html"].values[0]
    extreme_ownership_count = data.loc["extreme_ownership.html"].values[0]
    relentless_count = data.loc["relentless.html"].values[0]
    think_and_grow_rich_count = data.loc["think_and_grow_rich.html"].values[0]
    data.loc["index.html"] += 1
    data.to_csv(data_path)
    return render_template("index.html", visitor_count=visitor_count, deep_work_count=deep_work_count, how_to_win_friends_count = how_to_win_friends_count, cant_hurt_me_count = cant_hurt_me_count, atomic_habits_count = atomic_habits_count,
    extreme_ownership_count = extreme_ownership_count, relentless_count = relentless_count, think_and_grow_rich_count = think_and_grow_rich_count )

@app.route("/deep_work")
def deep_work():
    data_path = "/home/samurei/mysite/static/data/visits.csv"
    data = pd.read_csv(data_path, index_col="Page")

    data.loc["deep_work.html"] += 1
    data.to_csv(data_path)
    return render_template("deep_work.html")

@app.route("/how_to_win_friends")
def how_to_win_friends():
    data_path = "/home/samurei/mysite/static/data/visits.csv"
    data = pd.read_csv(data_path, index_col="Page")
    data.loc["how_to_win_friends.html"] += 1
    data.to_csv(data_path)
    return render_template("how_to_win_friends.html")

@app.route("/cant_hurt_me")
def cant_hurt_me():
    data_path = "/home/samurei/mysite/static/data/visits.csv"
    data = pd.read_csv(data_path, index_col="Page")
    data.loc["cant_hurt_me.html"] += 1
    data.to_csv(data_path)
    return render_template("cant_hurt_me.html")

@app.route("/atomic_habits")
def atomic_habits():
    data_path = "/home/samurei/mysite/static/data/visits.csv"
    data = pd.read_csv(data_path, index_col="Page")
    data.loc["atomic_habits.html"] += 1
    data.to_csv(data_path)
    return render_template("atomic_habits.html")

@app.route("/extreme_ownership")
def extreme_ownership():
    data_path = "/home/samurei/mysite/static/data/visits.csv"
    data = pd.read_csv(data_path, index_col="Page")
    data.loc["extreme_ownership.html"] += 1
    data.to_csv(data_path)
    return render_template("extreme_ownership.html")

@app.route("/relentless")
def relentless():
    data_path = "/home/samurei/mysite/static/data/visits.csv"
    data = pd.read_csv(data_path, index_col="Page")
    data.loc["relentless.html"] += 1
    data.to_csv(data_path)
    return render_template("relentless.html")

@app.route("/think_and_grow_rich")
def think_and_grow_rich():
    data_path = "/home/samurei/mysite/static/data/visits.csv"
    data = pd.read_csv(data_path, index_col="Page")
    data.loc["think_and_grow_rich.html"] += 1
    data.to_csv(data_path)
    return render_template("think_and_grow_rich.html")

@app.route("/contact", methods = ["GET","POST"])
def contact():
    data_path = "/home/samurei/mysite/static/data/contact.csv"
    data = pd.read_csv(data_path)
    if request.method == "POST":
        name = request.form["firstname"]
        message = request.form["subject"]
        new_row = {"name":name, "message":message}
        data = data.append(new_row, ignore_index=True)
        data.to_csv(data_path)
        return render_template("feedback_collected.html")
    else:
        return render_template("contact.html")

@app.route("/contact/feedback_collected")
def feedback():
    return render_template("feedback_collected.html")

if __name__ == "__main__":
    app.run()
