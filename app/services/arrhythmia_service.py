from app.models.arrhythmia_model import ArrhythmiaModel


class ArrhythmiaService:
    def __init__(self):
        self.arrhythmia_model = ArrhythmiaModel()

    def predict_arrhythmia(self, heartbeat_data):
        # Perform any necessary processing on heartbeat_data
        prediction = self.arrhythmia_model.predict_arrhythmia(heartbeat_data)
        return prediction
