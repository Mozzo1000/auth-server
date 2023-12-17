from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

jwt = JWTManager(app)

@app.route("/")
def index():
    return {
        "name": "example-auth-server-test",
        "version": "1.0.0"
    }

@app.route("/protected")
@jwt_required()
def protected():
    return {
        "name": "example-auth-server-test",
        "version": "1.0.0",
        "path": "protected"
    }

app.run(port=5001)