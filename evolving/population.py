# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class Population:
    nbCreated = 0
    num_gen_act = 0
    
    def __init__(self, size, percent_selection, chance_mutation, species, species_repartition, name="", nb_thread=1):
        
        for s in species:
            if getTopLevelParentClassAfterObject(s) != "Specie":
                raise NotASpecie("", "species need to be a Specie list")
                
        self.nbCreated += 1
        
        self.id = self.nbCreated
        self.name = name
        
        self.nextGen = []
        self.actualGen = []
        self.num_gen_act = 0
        
        self.size = []
        self.percent_selection = percent_selection
        self.chance_mutation = chance_mutation
        self.species = species
        self.species_repartition = species_repartition
        
        self.nbThread = nb_thread

    def getIdentification(self):
        if self.name == "":
            return self.id
        else:
            return self.name
        
    def getEntitiesFitness(self):
        return [e.getSpecie().entity_fitness(e) for e in self.actualGen]
    
    def getEntitiesDictionnaries(self):
        return [e.getDNA() for e in self.actualGen]
        
    def createGeneration(self):
        self.num_gen_act += 1
        
        # first generation we need to create a set of entities --> need to use repartition of species
        if self.num_gen_act == 1 :
            self.actualGen = [Entity.randomParameters() for _ in range(self.size)]
        else:
            self.actualGen = self.nextGen
            self.nextGen = []
        
    def orderGeneration(self):
        pass
    
    def selectGeneration(self):
        pass
    
    def breedGeneration(self):
        pass
    
    def mutateGeneration(self):
        pass
    
    def runGeneration(self, environnement=Environnement()):
        if getTopLevelParentClassAfterObject(environnement) != "Environnement" :
            raise NotAnEnvironnement("", "environnement need to be an Environnement")
            
        pass