# -*- coding: utf-8 -*-

from . import constantes

class NotAList(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class NotADictionnary(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class NotAPercent(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class PercentRepartitionIncorrect(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class NotASpecieCaracteristiqueDictionnary(Exception):
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

class UnknownReproductionType(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message 