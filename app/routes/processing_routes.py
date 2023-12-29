from flask import Blueprint, request, jsonify
from .. import socketio
from . import processing_routes
from app.services import ArrhythmiaService

arrhythmia_service = ArrhythmiaService()


@processing_routes.route("/heartbeat", methods=["POST"])
def receive_heartbeat_data():
    try:
        data = request.json  # Assuming data is sent as JSON in the request payload
        heartbeat_data = data.get("heartbeat_data")
        prediction = arrhythmia_service.predict_arrhythmia(heartbeat_data)

        # Send both prediction and heartbeat data to frontend using SocketIO
        socketio.emit(
            "prediction", {"prediction": prediction, "heartbeat_data": heartbeat_data}
        )

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
