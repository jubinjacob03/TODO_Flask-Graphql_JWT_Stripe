from modules.core import app
from database.schema import schema
from flask import jsonify, request
from modules.auth import private_route


@app.post("/users")
@private_route
def users_route(cur_user):
    data = request.get_json()
    query = data["query"]
    variables = data.get("variables")

    result = schema.execute(query, variable_values = variables)
    resp_data = {"data": result.data}

    if result.errors:
        resp_data['errors'] = [str(error) for error in result.errors]

    return jsonify(resp_data)
