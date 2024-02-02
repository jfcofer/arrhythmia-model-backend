import numpy as np
from keras.layers import Dense, Convolution1D, MaxPool1D, Flatten, Dropout
from keras.layers import Input
from keras.models import Model
from keras.layers import BatchNormalization

class ArrhythmiaModel:
    def __init__(self):
        self.model = ArrhythmiaModel
        data_path = '../assets/best_model.h5'
        im_shape = (186,1)
        inputs_cnn = Input(shape=(im_shape), name='inputs_cnn')
        conv1_1 = Convolution1D(64, (6), activation='relu', input_shape=im_shape)(inputs_cnn)
        conv1_1 = BatchNormalization()(conv1_1)
        pool1 = MaxPool1D(pool_size=(3), strides=(2), padding="same")(conv1_1)
        conv2_1 = Convolution1D(64, (3), activation='relu', input_shape=im_shape)(pool1)
        conv2_1 = BatchNormalization()(conv2_1)
        pool2 = MaxPool1D(pool_size=(2), strides=(2), padding="same")(conv2_1)
        conv3_1 = Convolution1D(64, (3), activation='relu', input_shape=im_shape)(pool2)
        conv3_1 = BatchNormalization()(conv3_1)
        pool3 = MaxPool1D(pool_size=(2), strides=(2), padding="same")(conv3_1)
        flatten = Flatten()(pool3)
        dense_end1 = Dense(64, activation='relu')(flatten)
        dense_end2 = Dense(32, activation='relu')(dense_end1)
        main_output = Dense(5, activation='softmax', name='main_output')(dense_end2)

        model = Model(inputs= inputs_cnn, outputs=main_output)
        model.compile(optimizer='adam', loss='categorical_crossentropy',metrics = ['accuracy'])
        model.load_weights(data_path)


    def predict_arrhythmia(self, data):
        class_labels = ['N', 'S', 'V', 'F', 'Q']
        dataArr = np.expand_dims(data, axis=0)

        results = self.model.predict(dataArr)
        single_result = results[0] # 0 ya que únicamente tiene ese valor
        most_likely_class_index = int(np.argmax(single_result))
        class_likelyhood = single_result[most_likely_class_index]

        class_label = class_labels[most_likely_class_index]
        return class_label, class_likelyhood
