from flask import Blueprint, make_response, jsonify, request
from src.modules.docker import Server
from src.modules.db.servers import ServerDB

server_routes_bp = Blueprint("servers", __name__)


@server_routes_bp.route("/servers", methods=["GET"])
def get_servers_list():
    respose = None
    try:
        respose = ServerDB.get_servers()
        return make_response(jsonify({"Response": respose}), 200)
    except Exception as exception:
        return make_response(jsonify({"Error": str(exception)}), 500)


@server_routes_bp.route("/servers", methods=["POST"])
def add_server():
    data = request.get_json()
    response = None
    try:
        new_server = ServerDB(
            ip=data["ip"],
            port=data["port"],
            name=data["name"]
        )
        id = new_server.add_server()
        new_server.id = id
        response = new_server.__dict__
        return make_response(jsonify({"Response": response}), 201)
    except Exception as exception:
        return make_response(jsonify({"Error": str(exception)}), 500)
