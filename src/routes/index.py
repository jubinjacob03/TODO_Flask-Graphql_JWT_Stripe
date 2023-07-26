from modules.core import app 
from flask import request, render_template

@app.get("/")
def index():
    auth_url = f"{request.root_url}login"

    return render_template(
        "index.html",
        auth_url = auth_url
    )