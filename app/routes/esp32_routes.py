from flask import Blueprint, request, jsonify
from flask_socketio import emit
from . import socketio

esp32_routes = Blueprint("esp32_routes", __name__)


@esp32_routes.route("/connect", methods=["POST"])
def connect_esp32():
    global esp32_connected

    # Check if ESP32 is already connected
    if esp32_connected:
        return jsonify({"message": "Already connected to ESP32"})

    # Perform ESP32 connection logic (replace with your actual logic)
    try:
        # Your ESP32 connection code here
        # For example, open a serial connection, initialize Wi-Fi, etc.
        # ...

        esp32_connected = True
        # Notify the frontend that ESP32 is connected
        socketio.emit("esp32_connected", {"data": "ESP32 connected"})

        # Example: Send a welcome message to ESP32
        socketio.emit("esp32_message", {"message": "Welcome, ESP32!"})

        return jsonify({"message": "Connection established with ESP32"})
    except Exception as e:
        return jsonify({"message": f"Failed to connect to ESP32: {str(e)}"}), 500
