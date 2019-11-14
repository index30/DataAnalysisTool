from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPool2D
from keras.optimizers import Adam, SGD
from keras.layers.core import Dense, Activation, Dropout, Flatten
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler


class CNNModel():
    def __init__(self):
        pass
    #TODO Fix below codes
    # def __init__(self, **params):
    #     self.origin_X_train = params["X_train"]
    #     self.origin_X_test = params["X_test"]
    #     self.result_X_train = params["X_train"]
    #     self.result_X_test = params["X_test"]
    
    # def define_model(self):
    #     model = Sequential()

    #     model.add(Conv2D(32,2,input_shape=(32,32,1)))
    #     model.add(Activation('relu'))
    #     # model.add(MaxPool2D(pool_size=(2,2)))

    #     model.add(Conv2D(32,2))
    #     model.add(Activation('relu'))
    #     model.add(MaxPool2D(pool_size=(2,2)))

    #     model.add(Conv2D(64,2,input_shape=(32,32,1)))
    #     model.add(Activation('relu'))
    #     # model.add(MaxPool2D(pool_size=(2,2)))

    #     model.add(Conv2D(64,2))
    #     model.add(Activation('relu'))
    #     model.add(MaxPool2D(pool_size=(2,2)))

    #     # model.add(Conv2D(64,3))
    #     # model.add(Activation('relu'))
    #     # model.add(MaxPool2D(pool_size=(2,2)))

    #     model.add(Flatten())
    #     model.add(Dense(512))
    #     model.add(Activation('relu'))
    #     model.add(Dropout(0.1))

    #     model.add(Dense(1, activation='sigmoid'))

    #     adam = Adam(lr=1e-4)
    #     sgd = SGD(lr=1e-5)

    #     model.compile(optimizer=adam, loss='binary_crossentropy', metrics=["accuracy"])
        
    #     return model
    
    # def reshape_data(self):
    #     self.result_X_train = self.result_X_train.values
    #     self.result_X_test = self.result_X_test.values
    #     self.result_X_train = self.result_X_train.astype('float32')
    #     self.result_X_test = self.result_X_test.astype('float32')
        
    #     tmp_X_train = []
    #     tmp_X_test = []
        
    #     ms = MinMaxScaler()
    #     X_train = ms.fit_transform(X_train)
    #     X_test = ms.transform(X_test)

    #     for x_train in self.result_X_train:
    #         x_train = np.reshape(x_train, (32, 32))
    #         x_train = x_train[:, :, np.newaxis]
    #         tmp_X_train.append(x_train)
    #     for x_test in self.result_X_test:
    #         x_test = np.reshape(x_test, (32, 32))
    #         x_test = x_test[:, :, np.newaxis]
    #         tmp_X_test.append(x_test)
            
    #     self.result_X_train = np.array(tmp_X_train)
    #     self.result_X_test = np.array(tmp_X_test)
        
    # def fit_predict(self, model, y_train, y_test):
    #     history = model.fit(self.result_X_train, y_train, batch_size=16, nb_epoch=30, verbose=1, validation_split=0.1)
    #     result = model.predict(self.result_X_test)
    #     print(mean_squared_error(result, y_test))

if __name__ == "__main__":
    cnn = CNNModel()
        