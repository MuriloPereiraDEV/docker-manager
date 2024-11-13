from flask import Blueprint, make_response, jsonify, request
from Back.src.modules.db.users import UserDB

users_routes_bp = Blueprint("users", __name__)


@users_routes_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    response = None
    try:
        new_user = UserDB(
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            password=data["password"]
        )
        new_user_id = new_user.create_user()
        new_user.id = new_user_id
        response = new_user.__dict__
        return make_response(jsonify({"Response": response}), 200)
    except Exception as exception:
        return make_response(jsonify({"Error": str(exception)}), 500)
