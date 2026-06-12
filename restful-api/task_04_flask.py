#!/usr/bin/python3
"""Simple Flask API with user management endpoints."""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Serve the API welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return a JSON list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return API status."""
    return "OK"


@app.route("/users/<username>")
def show_user_profile(username):
    """Get user by username or 404."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """POST new user or error 400/409."""
    user_data = request.get_json(silent=True)

    if user_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
