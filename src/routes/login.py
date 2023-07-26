from modules.core import app, db, UsersTable
from flask import request, make_response, jsonify, render_template, url_for
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
import os
import jwt


@app.get("/login")
def login_get():
    register_url = url_for("register_get")

    return render_template("login.html", register_url = register_url)


@app.post("/login")
def login_post():
    data = request.form
    email, password = data.get("email"), data.get("password")

    if not data or not email or not password:
        return make_response(
            jsonify({ "message": "Login Required!" }),
            401
        )

    user = UsersTable.query.filter_by(email = email).first()

    if not user:
        return make_response(
            jsonify({ "message": "User doesn't exist!" }),
            401
        )
    
    if check_password_hash(user.pass_hash, password):
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
        return make_response(
            jsonify({ "message": "Wrong password!" }),
            403
        )
