from app.services.arrhythmia_service import ArrhythmiaService
from app.socketio import socketio
from flask_socketio import emit
from flask import session

arrhythmia_service = ArrhythmiaService

@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on("heartbeat_input")
def handle_new_data(data):
    transmision = False
    if session.get("transmision"):
        transmision = session.get("transmision")
    if transmision:
        heartbeat_data = data["heartbeat_data"]
        prediction = arrhythmia_service.predict_arrhythmia(heartbeat_data)
        emit(
            "heartbeat_output",
            {"prediction": prediction, "heartbeat_data": heartbeat_data},
        )


@socketio.on("stop_transmision")
def handle_stop():
    session["transmision"] = False
    transmision = False


@socketio.on("start_transmision")
def handle_start():
    session["transmision"] = False
    transmision = True
