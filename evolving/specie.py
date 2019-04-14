# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class Specie:
    nbCreated = 0
    def __init__(self, fitness, name=""):
        if str(constantes.getTopLevelParentClassAfterObject(fitness)) != "Fitness":
            raise exceptions.NotAFitness("", "fitness need to be a Fitness")
        
        self.nbCreated += 1
        
        self.id = self.nbCreated
        self.name = name
        self.fitness = fitness
    
    def getId(self):
        return self.id
    
    def equals(self, specie):
        if str(constantes.getTopLevelParentClassAfterObject(specie)) != "Specie":
            raise exceptions.NotAFitness("", "specie need to be a Specie")
            
        return self.id == specie.getId()
    
    def compatibiliy(self, specie):
        if str(constantes.getTopLevelParentClassAfterObject(specie)) != "Specie":
            raise exceptions.NotAFitness("", "specie need to be a Specie")
        pass
    
    def mixDNA(DNA1, DNA2):
        #mix the 2 DNA and return a new DNA
        if str(type(DNA1)) != "dict" or str(type(DNA2)) != "dict":
            raise exceptions.NotADictionnary("", "DNA need to be a dictionnary")
        pass