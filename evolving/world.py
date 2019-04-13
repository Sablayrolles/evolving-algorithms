# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class World:
    def __init__(self, environnement, populations_list, name = ""):
        if getTopLevelParentClassAfterObject(environnement) != "Environnement" :
            raise NotAnEnvironnement("", "environnement need to be an Environnement")
            
        for p in populations_list:
            if getTopLevelParentClassAfterObject(p) != "Population" :
                raise NotAPopulation("", "populations_list need to be an Population list")
        
        self.name = name
        self.environnement = environnement
        self.populations = populations_list
        self.statistiques = {p.getIdentification() : Statistique(p) for p in self.populations}
    
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