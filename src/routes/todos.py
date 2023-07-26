from modules.core import app
from database.schema import schema
from flask import jsonify, request
from modules.auth import private_route
import graphql
from graphql.language import ast


def add_input_field_to_query(query_string, input_field_name, input_field_value):
    # Parse the query string into an Abstract Syntax Tree (AST)
    document_ast = graphql.parse(query_string)

    # Define the new input field
    new_input_field = ast.ObjectField(
        name=ast.Name(value=input_field_name),
        value=ast.StringValue(value=input_field_value),
    )

    # Find the operation definition you want to modify (in this case, we assume it's the first one)
    operation_definition = document_ast.definitions[0]

    # Find the field you want to add the input to (in this case, we assume it's the first one)
    field = operation_definition.selection_set.selections[0]

    # Add the new input field to the existing field's arguments
    if isinstance(field, ast.Field):
        field.arguments.append(new_input_field)

    # Print the modified query (optional)
    modified_query_string = graphql.print_ast(document_ast)
    print(modified_query_string)

    # Return the modified query as a string
    return modified_query_string



@app.post("/todos")
@private_route
def todos_route(cur_user):
    data = request.get_json()
    query = data["query"]
    variables = data.get("variables")

    query = add_input_field_to_query(query, "userId", cur_user.id)

    result = schema.execute(query, variable_values = variables)
    resp_data = { "data": result.data }

    if result.errors:
        resp_data['errors'] = [str(error) for error in result.errors]

    return jsonify(resp_data)