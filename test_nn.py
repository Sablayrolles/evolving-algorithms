#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:06:49 2019

@author: louis
"""

from keras.models import Sequential
from keras.layers import Dense

import numpy
import random

class NeuralNetwork:
    #parameters in agent : nbIn = percept, nbOut = nb actions, activation by list ?, type ??=> conv or others --> pb mix entre deux res de neurones
    def __init__(self, nbIn, typeIn, activationIn, nbOut, typeOut, activationOut, nbInt=[], activationInt=[], typeInt=[]):
        model = Sequential()
        
        
        #type:
        """
        Conv1D(nb, kernel-size=1, activation=)
        MaxPooling1D(pool-size=) # de combien on veut réduire si 800 au début et 400 a la fin alors =2
        RNN(nb)
        GRU(nb, activation=, recurrent-activation=)
        LSTM(nb, activation=, recurrent-activation=)
        """
        if typeIn == "Dense":
            model.add(Dense(int(nbIn), input_dim=nbIn, activation=activationIn))
            
        #implement int
        for nb, typ, act in zip(nbInt, typeInt, activationInt):
            if typ == "Dense":
                model.add(Dense(int(nb), activation=act))
                
        if typeOut == "Dense":
            model.add(Dense(int(nbOut), activation=activationOut))
        
        model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
            
        self.model = model
        
        #model.summary()
        
    def setActions(self, actions):
        self.actions = actions
        
    def predict(self, env=[], ret="name"):
        n = int(self.model.predict_classes(numpy.array([env])))
        if ret == "name":
            return self.actions[n]
        else:
            return n

n = NeuralNetwork(3, "Dense", "relu", 4, "Dense", "sigmoid", [8,15,15,8], ["relu", "relu", "relu", "relu"], ["Dense", "Dense", "Dense", "Dense", "Dense"])
n.setActions(["forward", "turnLeft", "turnRight", "backward"])
for i in range(15):
    t = [random.randint(0,15),random.randint(0,15),random.randint(0,15)] #on prédit sur [tab of parameters] :: car on peut vouloir faire plusieurs prédictions ...
    print("data:", t)
    print("action predicted : ")
    a = n.predict(t)
    print(a) #0->3s"""