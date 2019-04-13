# -*- coding: utf-8 -*-

from . import constantes

class NotADictionnary(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class NotAnEntity(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class NotAnEnvironnement(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class NotAPopulation(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class NotAFitness(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message 
        
class NotASpecie(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message 