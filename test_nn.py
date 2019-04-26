#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:06:49 2019

@author: louis
"""

from keras.models import Sequential
from keras.layers import Dense

import numpy

model = Sequential()

model.add(Dense(3, input_dim=3, activation="relu")) #input dim : nombre de parametres capteurs en entree
model.add(Dense(8, activation="relu"))
model.add(Dense(15, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(4, activation="tanh"))

model.summary()

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

t = numpy.array([[1,2,3]]) #on prédit sur [tab of parameters] :: car on peut vouloir faire plusieurs prédictions ...
print("data:", t)
print("action predicted : ")
a = model.predict_classes(t)
print(a) #0->3