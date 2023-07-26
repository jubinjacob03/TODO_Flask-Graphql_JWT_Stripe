from flask import render_template, request
from modules.core import app, checkout_sessions, db, UsersTable


@app.route("/premium/success")
def premium_success():
    print(checkout_sessions)

    session_id = request.args.get("session_id")
    user_id = checkout_sessions.get(session_id)
    del checkout_sessions[session_id]

    user: UsersTable = db.session.query(UsersTable).filter_by(id=user_id).first()

    if user:
        user.premium = True
        db.session.commit()


    return render_template("premium-success.html")