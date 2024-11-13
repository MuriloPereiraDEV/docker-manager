from flask import Blueprint, make_response, jsonify, request
from Back.src.modules.db.users import UserDB

login_routes_bp = Blueprint("login", __name__)


@login_routes_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response = None
    try:
        user_to_verify = UserDB(
            email=data["email"],
            password=data["password"]
        )
        existy_user = user_to_verify.verify_user()
        if existy_user:
            print(existy_user)
            response = UserDB(
                id=existy_user[0],
                email=existy_user[1],
                first_name=existy_user[2],
                last_name=existy_user[3]
            ).__dict__
            return make_response(jsonify({"Response": response}), 200)
        return make_response(jsonify({"Response": "User not found"}), 404)
    except Exception as exception:
        return make_response(jsonify({"Error": str(exception)}), 500)
