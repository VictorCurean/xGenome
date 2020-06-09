from flask import Blueprint, request, Response, jsonify
from xgenom.flaskserver.utils.utils import generate_salt, generate_hash, validate_user_input, db_write, validate_user, persist_token

authentication = Blueprint("authentication", __name__)

# @authentication.route("/register", methods=["POST"])
# def register_user():
#     pass
#
# @authentication.route("/login", methods=["POST"])
# def login_user():
#     pass

@authentication.route("/register", methods=["POST"])
def register_user():
    username = request.json["username"]
    user_password = request.json["password"]
    user_confirm_password = request.json["confirm_password"]

    if user_password == user_confirm_password and validate_user_input(
        "authentication", username=username, password=user_password
    ):
        password_salt = generate_salt()
        password_hash = generate_hash(user_password, password_salt)

        if db_write(
            """INSERT INTO users_auth (username, password_salt, password_hash) VALUES (%s, %s, %s)""",
            (username, password_salt, password_hash),
        ):
            # Registration Successful
            return Response(status=201)
        else:
            # Registration Failed
            return Response(status=409)
    else:
        # Registration Failed
        return Response(status=400)

@authentication.route("/login", methods=["POST"])
def login_user():
    username = request.json["username"]
    user_password = request.json["password"]

    user_token = validate_user(username, user_password)

    if user_token:
        persist_token(username, user_token)
        return jsonify({"jwt_token": user_token})

    else:
        return Response(status=401)