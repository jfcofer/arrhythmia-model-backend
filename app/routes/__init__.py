# app/routes/__init__.py
from flask_restx import Api

# Import your API routes
from app.routes.esp32_routes import esp32_namespace
from app.routes.processing_routes import processing_namespace

# Create an instance of Flask-RESTx Api
api = Api()

# Add the routes to the API instance
api.add_namespace(esp32_namespace)
api.add_namespace(processing_namespace)