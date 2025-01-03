from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from api.models import db, ma
from api.config import DevConfig, ProdConfig
import os
from api.routes.auth import auth_endpoint
from api.routes.user import user_endpoint
from api.commands.user import user_command

app = Flask(__name__)
CORS(app)
if os.environ.get("FLASK_DEBUG") == "1":
    app.config.from_object(DevConfig)
else:
    app.config.from_object(ProdConfig)

db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(auth_endpoint)
app.register_blueprint(user_endpoint)

app.register_blueprint(user_command)

@app.route("/")
def index():
    return {
        "name": "auth-server",
        "version": "1.0.0"
    }