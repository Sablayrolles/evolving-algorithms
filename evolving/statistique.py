# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class Statistique:
    def __init__(self, population):
        if str(constantes.getTopLevelParentClassAfterObject(population)) != "Population" :
            raise exceptions.NotAPopulation("", "population need to be an Population")
            
        self.targetPopulation = population
        
        self.data = []
        
        self.numGen = 0
        
    def fetchInformationsGeneration(self):
        self.data.append({"gennum": self.numGen, "fitness": self.targetPopulation.getEntitiesFitness(),  "entities": self.targetPopulation.getEntitiesDictionnaries()})
        
        self.numGen += 1
        
    def getAllInformations(self):
        return self.data