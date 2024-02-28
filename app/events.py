from app.services.arrhythmia_service import ArrhythmiaService
from app.socketio import socketio
from flask import session

arrhythmia_service = ArrhythmiaService


@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on("heartbeat_input")
def handle_new_data(data):
    transmission = False
    if session.get("transmission"):
        transmission = session.get("transmission")

    if transmission:
        heartbeat_data = data["heartbeat_data"]
        prediction = arrhythmia_service.predict_arrhythmia(heartbeat_data)
        socketio.emit(
            "heartbeat_output",
            {"prediction": prediction, "heartbeat_data": heartbeat_data},
        )


@socketio.on("stop_transmission")
def handle_stop():
    session["transmission"] = False


@socketio.on("start_transmission")
def handle_start():
    session["transmission"] = True
