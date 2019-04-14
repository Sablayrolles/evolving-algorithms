# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class World:
    def __init__(self, environnement, populations_list, statistiquesPopulationDict, name = ""):
        if str(constantes.getTopLevelParentClassAfterObject(environnement)) != "Environnement" :
            raise exceptions.NotAnEnvironnement("", "environnement need to be an Environnement")
            
        for p in populations_list:
            if str(constantes.getTopLevelParentClassAfterObject(p)) != "Population" :
                raise exceptions.NotAPopulation("", "populations_list need to be an Population list")
        
        if str(type(statistiquesPopulationDict)) != "dict":
             raise exceptions.NotADictionnary("","statistiquesPopulationDict need to be a dictionnary Population : Statistique")
             
        for p,s in statistiquesPopulationDict.items():
            if str(constantes.getTopLevelParentClassAfterObject(p)) != "Population":
                 raise exceptions.NotAPopulation("", "population in statistiquesPopulationDict need to be Population")
                 
            if str(constantes.getTopLevelParentClassAfterObject(p)) != "Statistique":
                 raise exceptions.NotAPopulation("", "statistique in statistiquesPopulationDict need to be Statistique")
                 
        self.name = name
        self.environnement = environnement
        self.populations = populations_list
        self.statistiques = {}
    
    def tick(self):
        self.environnement.tick()
        
        for p in self.populations:
            p.createGeneration()
        
        #in parallela
        for p in self.populations:
            p.runGeneration()
            
        for p in self.populations:
            p.orderGeneration()
            p.selectGeneration()
            p.breedGeneration()
            p.mutateGeneration()