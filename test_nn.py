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
    def __init__(self, nbIn, nbOut, nbInt=[], activationIn, activationOut, activationInt=[], typeIn, typeOut, typeInt=[]):
        self.model = Sequential()
        
        if typeIn == "Dense":
            self.model.add(Dense(nbIn, input_dim=nbIn, activation=activationIn))
            
        #implement int
            
        if typeOut == "Dense":
            self.model.add(Dense(nbOut, activation=activationOut))
            
        self.model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
            
    def setActions(self, actions):
        self.actions = actions
        
    def predict(self, env=[]):
        return self.actions[self.model.predict([env])]

model = Sequential()

model.add(Dense(3, input_dim=3, activation="relu")) #input dim : nombre de parametres capteurs en entree
model.add(Dense(8, activation="relu"))
model.add(Dense(15, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(4, activation="tanh"))

model.summary()

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

for i in range(15):
    t = numpy.array([[random.randint(-5,5),random.randint(-5,5),random.randint(-5,5)]]) #on prédit sur [tab of parameters] :: car on peut vouloir faire plusieurs prédictions ...
    print("data:", t)
    print("action predicted : ")
    a = model.predict_classes(t)
    print(a) #0->3