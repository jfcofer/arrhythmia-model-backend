from flask import jsonify
from flask_restx import Namespace, Resource
from app.socketio import socketio


esp32_namespace = Namespace(
    "esp32",
    description="Ruta para establecer comunicacion con el ESP32, y activar los Web Sockets",
)


@esp32_namespace.route("/connect")
class ConnectESP32(Resource):
    @esp32_namespace.doc(
        responses={
            200: "Conexion establecida con el ESP32",
            500: "Fallos en la conexion con el ESP32",
        }
    )
    def post(self):
        esp32_connected = sessio
        react_connected

        # Check if ESP32 is already connected
        if esp32_connected and react_connected:
            return jsonify({"message": "Already connected to ESP32"})

        esp32_connected = False
        react_connected = False

        @socketio.emit("connection_request")

        @socketio.on("connection_response_esp32")
        def handle_connection_response_esp32():
            esp32_connected = True

        @socketio.on("connection_response_react")
        def handle_connection_response_react():
            react_connected = True

        if esp32_connected and react_connected:
            return jsonify({"message": "Connection established with ESP32"}), 200
        else:
            return jsonify({"message": "Failed to connect to ESP32"}), 500
