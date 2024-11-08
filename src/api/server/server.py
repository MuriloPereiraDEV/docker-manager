from flask import Flask
from flask_cors import CORS
from src.api.routes.containers import containers_routes_bp
from src.api.routes.servers import server_routes_bp
from src.api.routes.images import images_routes_bp
from src.api.routes.networks import networks_routes_bp
from src.api.routes.volumes import volumes_routes_bp

app = Flask(__name__)
CORS(app=app)

app.register_blueprint(containers_routes_bp)
app.register_blueprint(server_routes_bp)
app.register_blueprint(images_routes_bp)
app.register_blueprint(networks_routes_bp)
app.register_blueprint(volumes_routes_bp)
