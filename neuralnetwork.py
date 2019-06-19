#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:06:49 2019

@author: louis
"""

from keras.models import Sequential
from keras.layers import Dense, Conv1D, MaxPooling1D, GRU, LSTM

import numpy
import random

class NeuralNetwork:
    #parameters in agent : nbIn = percept, nbOut = nb actions, activation by list ?--> pb mix entre deux res de neurones
    def __init__(self, nbIn, activationIn, nbOut, activationOut, nbInt=[], activationInt=[]):
        model = Sequential()

        #activation: softmax, elu, selu, softplus, softsign, relu, tanh, sigmoid, hard_sigmoid, exponential, linear
       
        model.add(Dense(int(nbIn), input_dim=nbIn, activation=activationIn))

        #implement int
        for nb, act in zip(nbInt, activationInt):
            model.add(Dense(int(nb), activation=act))
        
        model.add(Dense(int(nbOut), activation=activationOut))
                  
        model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
            
        self.model = model
    
        model.summary()

    def listActivation():
        return ["softmax", "elu", "selu", "softplus", "softsign", "relu", "tanh", "sigmoid", "hard_sigmoid", "exponential", "linear"]

    def randomActivation():
        return random.choice(NeuralNetwork.listActivation())

    def randomNeuralNetwork(MAX_COUCHES, MAX_NN_COUCHES, nbIn, nbOut):
        nbCoucheInt = random.randint(0, MAX_COUCHES-2)
        
        return NeuralNetwork(nbIn, NeuralNetwork.randomActivation(), nbOut, NeuralNetwork.randomActivation(), [random.randint(1, MAX_NN_COUCHES)+1 for _ in range(nbCoucheInt)], [NeuralNetwork.randomActivation() for _ in range(nbCoucheInt)])

    def isSet(self):
        return "model" in self.__dict__.keys()
        
    def setActions(self, actions):
        self.actions = actions
        
    def predict(self, env=[], ret="name"):
        if "model" in self.__dict__.keys():
            n = int(self.model.predict_classes(numpy.array([env])))
            if ret == "name":
                return self.actions[n]
            else:
                return n
        else:  
            return False

"""n = NeuralNetwork.randomNeuralNetwork(15, 10, 3, 4)
n.setActions(["forward", "turnLeft", "turnRight", "backward"])
for i in range(15):
    t = [random.randint(0,15),random.randint(0,15),random.randint(0,15)] #on prédit sur [tab of parameters] :: car on peut vouloir faire plusieurs prédictions ...
    print("data:", t)
    print("action predicted : ")
    a = n.predict(t)
    print(a) #0->3s"""