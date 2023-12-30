from flask import jsonify
from flask_restx import Namespace, Resource
from app.socketio import socketio


esp32_namespace = Namespace("ESP32", description="Routes for ESP32 communication")


@esp32_namespace.route("/connect")
class ConnectESP32(Resource):
    @esp32_namespace.doc(responses={200: "Connection established with ESP32"})
    def post(self):
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
