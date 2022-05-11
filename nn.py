import tensorflow
from tensorflow import keras
from keras.layers import Dense
from keras.models import Model
from keras.layers import Sequential
import random

#creating a random neural network

def create_net():
    model = Sequential()
    model.add(keras.Input(shape=(4,)))
    model.add(Dense(random.randint(1, 5), activation = 'tanh'))
    model.add(Dense(1, activation = 'sigmoid'))
