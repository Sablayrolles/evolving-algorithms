# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

import statistics

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
    
    def getFitness(self):
        return {f["gennum"] : f["fitness"] for f in self.getAllInformations()}
        
    def getEntities(self):
        return {f["gennum"] : f["entities"] for f in self.getAllInformations()}
        
    def getFitnessStats(self):
        return {k: {"min": min(v), "max": max(v), "median": statistics.median(v), "mean": statistics.mean(v)} for k,v in self.getFitness().items()}