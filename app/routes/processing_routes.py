from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from .. import socketio
from . import processing_routes
from app.services import ArrhythmiaService

arrhythmia_service = ArrhythmiaService()

api = Namespace("Processing", description="Routes for processing heartbeat data")

# Define a model for request and response
heartbeat_model = api.model(
    "HeartbeatModel",
    {"heartbeat_data": fields.String(description="Raw heartbeat data")},
)


@api.route("/heartbeat")
class Heartbeat(Resource):
    @api.doc(responses={200: "Success"}, model=heartbeat_model)
    @api.expect(heartbeat_model)
    def post(self):
        try:
            data = request.json  # Assuming data is sent as JSON in the request payload
            heartbeat_data = data.get("heartbeat_data")
            prediction = arrhythmia_service.predict_arrhythmia(heartbeat_data)

            # Send both prediction and heartbeat data to frontend using SocketIO
            socketio.emit(
                "prediction",
                {"prediction": prediction, "heartbeat_data": heartbeat_data},
            )

            return jsonify({"success": True})
        except Exception as e:
            return jsonify({"success": False, "error": str(e)})
