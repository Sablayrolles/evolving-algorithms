# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class Population:
    nbCreated = 0
    num_gen_act = 0
    
    def __init__(self, size, percent_selection, chance_mutation, percent_variation_mutation, species_caracteristiques, nb_thread=1):
        
        if str(type(species_caracteristiques)) != "<class 'list'>":
            print(str(type(species_caracteristiques)))
            raise exceptions.NotAList("", "species need to be a list of dictionnary")  
        
        s_percent = 0.0
        for e in species_caracteristiques:
            if str(type(e)) != "<class 'dict'>":
                raise exceptions.NotADictionnary("", "species_caracteristiques need to be a list of dictionnary")
            if "class" not in e.keys() or "specie" not in e.keys() or "percent" not in e.keys():
                raise exceptions.NotASpecieCaracteristiqueDictionnary("", "species_caracteristiques need to be a list of dictionnary with class: ClassEntitéeReferenceInAVariable (like pointer), specie: variable of type specie and percent: float of repartition")
            
            classe = e["class"]
            specie = e["specie"]
            percent = e["percent"]
            
            var = classe.randomParameters(specie)
            if str(constantes.getTopLevelParentClassAfterObject(var)) != "Entity" :
                raise exceptions.NotAnEnvironnement("", "entities in species_caracteristiques need to be an Entity class reference")
            if str(constantes.getTopLevelParentClassAfterObject(specie)) != "Specie" :
                raise exceptions.NotAnEnvironnement("", "species in species_caracteristiques need to be an Specie")
            if str(type(percent)) != "<class 'int'>" and str(type(percent)) != "<class 'float'>":
                print(type(percent))
                raise exceptions.NotAPercent("", "percent in species_caracteristiques need to be an int or a float")
            
            s_percent += float(percent) 
        if s_percent != 1:
            raise exceptions.PercentRepartitionIncorrect("", "sum of percent repartition need to be equals to 100")
            
        self.nbCreated += 1
        
        self.id = self.nbCreated
        
        self.nextGen = []
        self.actualGen = []
        self.num_gen_act = 0
        
        self.size = size
        self.percent_selection = percent_selection
        self.chance_mutation = chance_mutation
        self.percent_variation_mutation = percent_variation_mutation
        self.species_caracteristiques = species_caracteristiques
        
        self.nbThread = nb_thread
        
        self.order = []
        self.selectGen = []

    def getIdentification(self):
        if self.name == "":
            return self.id
        else:
            return self.name
        
    def getEntitiesFitness(self):
        return [e.getSpecie().getEntityFitness(e) for e in self.actualGen]
    
    def getEntitiesDictionnaries(self):
        return [e.getDNA() for e in self.actualGen]
        
    def createGeneration(self):
        self.num_gen_act += 1
        
        # first generation we need to create a set of entities --> need to use repartition of species
        if self.num_gen_act == 1 :
            self.actualGen = []
            for e in self.species_caracteristiques: 
                classe = e["class"]
                specie = e["specie"]
                percent = e["percent"]
                
                self.actualGen.extend([classe.randomParameters(specie) for _ in range(int(float(percent) * self.size ))])
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
    
    def runGeneration(self, environnement):
        if str(constantes.getTopLevelParentClassAfterObject(environnement)) != "Environnement" :
            raise exceptions.NotAnEnvironnement("", "environnement need to be an Environnement")
            
        pass