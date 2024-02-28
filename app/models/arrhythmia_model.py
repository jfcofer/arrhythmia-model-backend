import numpy as np
from keras.models import load_model

class ArrhythmiaModel:
    def __init__(self):
        model_filepath = "model.keras"
        self.model = load_model(model_filepath)

    def predict_arrhythmia(self, data):
        class_labels = ['N', 'S', 'V', 'F', 'Q']
        dataArr = np.expand_dims(data, axis=0)

        results = self.model.predict(dataArr)
        single_result = results[0] # 0 ya que únicamente tiene ese valor
        most_likely_class_index = int(np.argmax(single_result))
        class_likelyhood = single_result[most_likely_class_index]

        class_label = class_labels[most_likely_class_index]
        return class_label, class_likelyhood
