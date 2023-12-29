# app/__init__.py
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
from .config import Config
from .routes.esp32_routes import esp32_routes
from .routes.processing_routes import processing_routes
import logging
from logging.handlers import RotatingFileHandler

socketio = SocketIO(cors_allowed_origins="*")


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Initialize SocketIO
    socketio.init_app(app)

    # Import and register the routes

    app.register_blueprint(esp32_routes, url_prefix="/api/esp32")
    app.register_blueprint(processing_routes, url_prefix="/api/processing")

    # Initialize extensions or other setup code here
    # Custom error pages
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("500.html"), 500

    @socketio.on("connect")
    def handle_connect():
        print("Client connected")

    # Setup logging
    if not app.debug:
        handler = RotatingFileHandler(
            app.config["LOGGING_LOCATION"], maxBytes=10000, backupCount=1
        )

    return app
