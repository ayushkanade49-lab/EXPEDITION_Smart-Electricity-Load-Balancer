from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Demo users (same as your HTML)
users = [
    {"email": "rajan@gmail.com", "password": "pass123"},
    {"email": "kumar@gmail.com", "password": "pass123"},
    {"email": "suresh@gmail.com", "password": "pass123"},
    {"email": "mohan@gmail.com", "password": "pass123"},
    {"email": "vikram@gmail.com", "password": "pass123"},
    {"email": "prasad@gmail.com", "password": "pass123"},
    {"email": "naveen@gmail.com", "password": "pass123"},
    {"email": "deepak@gmail.com", "password": "pass123"},
    {"email": "arun@gmail.com", "password": "pass123"},
    {"email": "manager@gmail.com", "password": "admin123"},
]

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email").strip()
    password = data.get("password").strip()

    # Validate user
    valid_user = next((u for u in users if u["email"] == email and u["password"] == password), None)

    if valid_user:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Invalid email or password"})


@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome to PowerGrid AI Dashboard ⚡</h1>"


if __name__ == "__main__":
    app.run(debug=True)