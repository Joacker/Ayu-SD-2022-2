from flask import jsonify
import bcrypt
from db.models import User
from db.models import db

def register_check(data):
    if not data:
        return jsonify({"error": "No data received"}), 400
    if User.query.filter_by(user=data.get('user')).first():
        return jsonify({"error": "User already exists"}), 400
    if len(data.get('pass')) < 8:
        return jsonify({"error": "Password too short"}), 400
    if len(data.get('user')) < 3:
        return jsonify({"error": "user too short"}), 400
    if not data.get('pass').isalnum():
        return jsonify({"error": "Password must contain letters and numbers"}), 400
    else:
        print("Entra al else")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(data.get('pass').encode('utf-8'), salt)
        user = User(
            password=hashed_password.decode('utf-8'), 
            user=data.get('user'), 
            )
        db.session.add(user)
        db.session.commit()
        return jsonify("User created correctly"), 201