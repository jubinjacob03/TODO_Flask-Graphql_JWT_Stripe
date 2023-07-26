from flask import render_template, request
from modules.core import app, checkout_sessions


@app.route("/premium/success")
def premium_cancel():
    session_id = request.args.get("session_id")
    user_id = checkout_sessions.get(session_id)

    

    render_template("premium-cancel.html")