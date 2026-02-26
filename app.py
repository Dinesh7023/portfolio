from flask import Flask, render_template, request, redirect, flash
import os
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Basic validation
    if not name or not email or not message:
        flash("All fields are required.")
        return redirect("/")

    # Email validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        flash("Invalid email address.")
        return redirect("/")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


