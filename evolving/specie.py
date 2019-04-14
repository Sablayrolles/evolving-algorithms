# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

import random

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
            raise exceptions.NotASpecie("", "specie need to be a Specie")
        pass
        # return number between 0 and 1 if 0 not compatible and if 1 totally compatible
        
        return random
    
    def mixDNAandCreatewithOthersSpecies(self, other_specie, DNA_of_member, DNA_of_other_specie):
        #mix the 2 DNA and return a new individual
        if str(type(DNA_of_member)) != "dict" or str(type(DNA_of_other_specie)) != "dict":
            raise exceptions.NotADictionnary("", "DNA need to be a dictionnary")
        
        if self.compatibility(other_specie) == 0:
            raise exceptions.NotCompatible("", "specie "+self.getId()+" and specie "+other_specie.getId()+ " are totally incompatible") 
        else:
            if random.random() > self.compatibility(other_specie):
                raise exceptions.UnviableReproduction("", "specie "+self.getId()+" and specie "+other_specie.getId()+ " reproduction fails please retry")
        pass