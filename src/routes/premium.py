import stripe
from modules.core import app, checkout_sessions
from flask import redirect, url_for
from modules.auth import private_route
from uuid import uuid4

@app.get("/premium")
@private_route
def premium_get(cur_user):
    print(cur_user.premium)

    session_id = uuid4()
    checkout_sessions[str(session_id)] = cur_user.id

    print(checkout_sessions)

    session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=['card'],
        line_items=[{
            "price": "price_1NXMfuSFGlTcxh6dMWOY1I5Y",
            "quantity": 1,
        }],
        success_url=url_for("premium_success", _external=True) + f'?session_id={session_id}',
        cancel_url=url_for("premium_cancel", _external=True),
    )

    return redirect(session.url, code=303)