# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class Statistique:
    def __init__(self, population):
        if str(constantes.getTopLevelParentClassAfterObject(population)) != "Population" :
            raise exceptions.NotAPopulation("", "population need to be an Population")
            
        self.targetPopulation = population
        
        self.data = []
        
    def fetchInformationsGeneration(self):
        self.data.append({"fitness": self.targetPopulation.getEntitiesFitness(),  "entities": self.targetPopulation.getEntitiesDictionnaries()})
        
    def getAllInformations(self):
        return self.data