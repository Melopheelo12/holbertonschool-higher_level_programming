#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ------------------------
# BASIC AUTHENTICATION
# ------------------------

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ------------------------
# JWT AUTHENTICATION
# ------------------------

@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON"}), 401

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    additional_claims = {"role": users[username]["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt_identity()
    from flask_jwt_extended import get_jwt

    jwt_data = get_jwt()
    role = jwt_data.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ------------------------
# JWT ERROR HANDLERS
# ------------------------

@jwt.unauthorized_loader
def handle_unauthorized(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(err):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run()
