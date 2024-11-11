from flask import Blueprint, make_response, jsonify
from Back.src.modules.docker import Server

images_routes_bp = Blueprint(
    'images', __name__, url_prefix='/servers/<id_server>/images')


@images_routes_bp.route("/", methods=['GET'])
def get_images_list(id_server):
    reponse = None
    current_server = None
    servers = [
        Server(id="abc123", ip="192.168.15.51",
                  port="2375", name="Servidor 1"),
        Server(id="def456", ip="192.42.37.92",
                  port="7777", name="Servidor 2"),
        Server(id="ghi789", ip="168.28.20.48",
                  port="7777", name="Servidor 3")
    ]
    try:
        for server in servers:
            if server.id == id_server:
                current_server = server
        if current_server:
            response = current_server.get_images()
            return make_response(jsonify({"Response": response}), 200)
        return make_response(jsonify({"Response": "Sem informações deste servidor!"}), 200)
    except Exception as exception:
        return make_response(jsonify({"Error": str(exception)}), 500)
