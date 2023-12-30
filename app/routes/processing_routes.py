from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.socketio import socketio
from app.services.arrhythmia_service import ArrhythmiaService

arrhythmia_service = ArrhythmiaService()

processing_namespace = Namespace(
    "Processing", description="Routes for processing heartbeat data"
)

# Define a model for request and response
heartbeat_model = processing_namespace.model(
    "HeartbeatModel",
    {"heartbeat_data": fields.String(description="Raw heartbeat data")},
)


@processing_namespace.route("/heartbeat")
class Heartbeat(Resource):
    @processing_namespace.doc(responses={200: "Success"}, model=heartbeat_model)
    @processing_namespace.expect(heartbeat_model)
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

