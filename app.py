from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

@app.route("/")
def root():
    return redirect("/dobrodosli-u-projekat")

@app.route("/dobrodosli-u-projekat")
def home():
    return render_template("index.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)







