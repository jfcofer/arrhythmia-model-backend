from app.services.arrhythmia_service import ArrhythmiaService
from app.socketio import socketio
from app.services import ConnectionManager
from app.services import TransmissionManager

connection_manager = ConnectionManager()

transmission_manager = TransmissionManager()

arrhythmia_service = ArrhythmiaService()


@socketio.on("connect")
def handle_connect():
    print("Client connected")


socketio.on("connection_response_esp32")(
    connection_manager.handle_connection_response_esp32
)

socketio.on("connection_response_client")(
    connection_manager.handle_connection_response_client
)


@socketio.on("heartbeat_input")
def handle_new_data(data):
    print(f"Data received {data}")
    if transmission_manager.is_transmitting:
        heartbeat_data = data["heartbeat_data"]
        prediction = arrhythmia_service.predict_arrhythmia(heartbeat_data)
        socketio.emit(
            "heartbeat_output",
            {"prediction": prediction, "heartbeat_data": heartbeat_data},
        )


@socketio.on("start_transmission")
def handle_start():
    transmission_manager.start_transmission()
    print("Transmission Enabled")


@socketio.on("stop_transmission")
def handle_stop():
    transmission_manager.stop_transmission()
    print("Transmission Disabled")
