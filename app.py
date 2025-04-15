from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials for validation
VALID_USERNAME = "user123"
VALID_PASSWORD = "pass123"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", error=None)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return f"Welcome, {username}!"
    else:
        error_message = "Invalid username or password!"
        return render_template("index.html", error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
