from modules.core import app
from flask import make_response, redirect, url_for


@app.get("/logout")
def logout_route():
    resp = make_response(redirect(url_for("login_get")))
    resp.delete_cookie("jwt_token")

    return resp