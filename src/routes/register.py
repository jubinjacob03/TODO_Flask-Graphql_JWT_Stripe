from modules.core import app, db, UsersTable
from flask import request, make_response, render_template, jsonify
from werkzeug.security import generate_password_hash
import uuid
from datetime import datetime, timedelta
import os
import jwt


@app.get("/register")
def register_get():
    return render_template("register.html")

@app.post("/register")
def register_post():
    data = request.form
    email, password = data.get("email"), data.get("password")

    exists = UsersTable.query.filter_by(email = email).first()

    if not exists:
        user = UsersTable(
            id = uuid.uuid4(),
            email = email,
            pass_hash = generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        expires = datetime.utcnow() + timedelta(days=7)
        token = jwt.encode(
            { "id": user.id, "pro": user.premium, "exp": expires },
            os.getenv("JWT_SECRET_KEY"),
            algorithm="HS256"
        )

        resp = make_response(jsonify({'token' : token}), 201)
        resp.set_cookie("jwt_token", token, expires=expires)

        return resp
    else:
        return make_response('User already exists. Please Log in.', 202)
