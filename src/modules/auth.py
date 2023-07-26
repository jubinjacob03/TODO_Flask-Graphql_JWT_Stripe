import os
import jwt
from flask import jsonify, request
from functools import wraps
from modules.core import UsersTable


# decorator for verifying the JWT
def private_route(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is present in the cookie
        token = request.cookies.get("jwt_token")

        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Bearer Token is missing!!'}), 401
        
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=["HS256"])
            current_user = UsersTable.query.filter_by(id = data['id']).first()
        except Exception as err:
            print(err)
            return jsonify({
                'message': 'Token is invalid!!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated