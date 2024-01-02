# app/__init__.py
from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api
from logging.handlers import RotatingFileHandler
from app.config import Config
from app.socketio import socketio
from app.routes import esp32_namespace, processing_namespace

api = Api()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Initialize Flask-RESTPlus
    api.init_app(app, doc="/api/docs")
    api.add_namespace(esp32_namespace)
    api.add_namespace(processing_namespace)

    # Custom error pages
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("500.html"), 500

    # Setup logging
    if not app.debug:
        handler = RotatingFileHandler(
            app.config["LOGGING_LOCATION"], maxBytes=10000, backupCount=1
        )

    socketio.init_app(app)

    @socketio.on("connect")
    def handle_connect():
        print("Client connected")

    return app, socketio
