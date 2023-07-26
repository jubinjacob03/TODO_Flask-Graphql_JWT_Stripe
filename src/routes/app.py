from flask import request, render_template
from modules.core import app, TodosTable
from modules.auth import private_route


@app.get("/app")
@private_route
def app_route(cur_user):
    user = {
        "id": cur_user.id,
        "email": cur_user.email,
        "premium": cur_user.premium
    }

    todos = []

    todoObjs = TodosTable.query.filter_by(user_id = cur_user.id).all()
    for todo in todoObjs:
        todos.append({
            "id": todo.id,
            "user_id": todo.user_id,
            "title": todo.title,
            "description": todo.description,
            "time": todo.time
        }) 


    return render_template("app.html", user = user, todos = todos)