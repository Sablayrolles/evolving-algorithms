# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions
from . import fitness

class Specie:
    nbCreated = 0
    def __init__(self, fitness, name=""):
        if getTopLevelParentClassAfterObject(fitness) != "Fitness":
            raise NotAFitness("", "fitness need to be a Fitness")
        self.nbCreated += 1
        
        self.id = self.nbCreated
        self.name = name
        self.fitness = fitness
    
    def getId(self):
        return self.id
    
    def equals(self, specie):
        if getTopLevelParentClassAfterObject(specie) != "Specie":
            raise NotAFitness("", "specie need to be a Specie")
            
        return self.id == specie.getId()
    
    def compatibiliy(self, specie):
        if getTopLevelParentClassAfterObject(specie) != "Specie":
            raise NotAFitness("", "specie need to be a Specie")
        pass
    
    def mixDNA(DNA1, DNA2):
        #mix the 2 DNA and return a new DNA
        if str(type(DNA1)) != "dict" or str(type(DNA2)) != "dict":
            raise NotADictionnary("", "DNA need to be a dictionnary")
        pass