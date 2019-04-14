# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class Entity:
    nbCreated = 0
    def __init__(self, specie, reproduction_type="clone", reproduction_max_child=-1): 
        # reproduction_type = ["clone", "replicated", "couple", "binary"]
        # clone: the individual make a copy of itself younger
        # replicated : the indicidual make a copy of itself
        # couple : the individual can reproduce only with a single entity only once (sameAsOldGeneration if not died)
        # binary : the individual can reproduce with any entity only once
        
        #reproduction_max_child = -1 : no limit
        if str(constantes.getTopLevelParentClassAfterObject(specie)) != "Specie":
            raise exceptions.NotASpecie("", "specie need to be a Specie")
            
        self.__class__.nbCreated += 1
        
        self.id = self.__class__.nbCreated
        self.specie = specie
        self.reproduction_type = reproduction_type
        self.reproduction_max_child = reproduction_max_child
        self.partener = None
        
        self.reproductionChildNumberOnTick = 0
        self.internclock = 0
        
    def getId(self):
        return self.id
    
    def equals(self, entity):
        if str(constantes.getTopLevelParentClassAfterObject(entity)) != "Entity" :
            raise exceptions.NotAnEntity("", "entity need to be an entity")
            
        return self.id == entity.getId()
    
    def getSpecie(self):
        return self.specie
    
    def getDNA(self):
        return self.__dict__.copy()
    
    def mixDNA(self, DNA1, DNA2):
        if str(type(DNA1)) != "<class 'dict'>" or str(type(DNA2)) != "<class 'dict'>":
            raise exceptions.NotADictionnary("", "DNAs need to be a dictionnary DNA1:"+str(type(DNA1))+", DNA2:"+str(type(DNA2)))
        pass
    
    def mutate(self, percent_mutation):
        pass
    
    def clone(self, reinitialiseInternalClock = True):
        DNA = self.getDNA()
        
        if reinitialiseInternalClock:
            DNA["internclock"] = 0
            
        return DNA
    
    def _initialize(self):
        pass
    
    def injectDNA(self, DNA, keepSameId = False):
        if str(type(DNA)) != "<class 'dict'>":
            raise exceptions.NotADictionnary("", "DNA need to be a dictionnary")
            
        self.__dict__ = DNA
        if not keepSameId:
            self.__class__.nbCreated += 1
            self.id = self.__class__.nbCreated
    
    def randomParameters(specie):
        return Entity(specie)
    
    def fitness(self):
        return self.specie.getEntityFitness(self)
    
    def reproduction_setPartner(self, entity):
        if str(constantes.getTopLevelParentClassAfterObject(entity)) != "Entity" :
            raise exceptions.NotAnEntity("", "entity need to be an entity")
            
        self.partener = entity
        
    def isSameSpecie(self, entity):
        if str(constantes.getTopLevelParentClassAfterObject(entity)) != "Entity" :
            raise exceptions.NotAnEntity("", "entity need to be an entity")
            
        return self.getSpecie().equals(entity.getSpecie())
        
    def checkIfReproductionIsPossible(self, entity):
        if str(constantes.getTopLevelParentClassAfterObject(entity)) != "Entity" :
            raise exceptions.NotAnEntity("", "entity need to be an entity")
            
        #to complete with test of sex parameters for exemple
        return True
    
    def reproduction_2_individuals(self, entity):
        if str(constantes.getTopLevelParentClassAfterObject(entity)) != "Entity" :
            raise exceptions.NotAnEntity("", "entity need to be an entity")
        
        #to complete with ::
        """
        use: MixDNA
        if self.checkIfReproductionIsPossible(entity):
            return Entity(entity.getSpecie())
        else:
            return None
        """
        pass
    
    def reproduce(self, entity=None, keepSameId=False): 
        #on check le nombre d'enfant
        if self.reproduction_max_child != -1 and self.reproductionChildNumberOnTick > self.reproduction_max_child:
            raise exceptions.CantReproduceDueToMaxChild("", "Too much child was create i can't reproduce"+self.reproduction_max_child+ "(set to -1 for no limit)")
        
        if self.reproduction_type == "clone":
            newEntity = self.__class__.randomParameters(self.getSpecie())
            newEntity.injectDNA(self.clone(), keepSameId = keepSameId)
            self.reproductionChildNumberOnTick += 1
            
            return newEntity
        else:
            newEntity = self.__class__.randomParameters(self.getSpecie())
            if self.reproduction_type == "replicated":
                newEntity.injectDNA(self.clone(reinitialiseInternalClock = False), keepSameId = keepSameId)
                self.reproductionChildNumberOnTick += 1
                
                return newEntity
            else:
                if self.reproduction_type == "couple":
                    if entity == None:
                        raise exceptions.ReproductionTwoIndividualNeedOtherEntity("", "entity need to be another member")
                            
                    #si le couple n'est pas créé on le créé:
                    if self.partener == None:
                        self.partener = entity
                        #et on créé la réplique chez le partener
                        entity.reproduction_setPartner(self)
                    
                    if entity.equals(self.partener):
                        if self.isSameSpecie(entity):
                            self.reproductionChildNumberOnTick += 1
                            
                            return self.reproduction_2_individuals(entity)
                        else:
                            self.reproductionChildNumberOnTick += 1
                            
                            return self.getSpecie().mixDNAandCreatewithOthersSpecies(entity.getSpecie(), self.getDNA(), entity.getDNA())
                    else:
                        raise exceptions.NotMyPartner("", "this is not my partner i can't reproduce with")
                else:
                    if self.reproduction_type == "binary":
                        if entity == None:
                            raise exceptions.ReproductionTwoIndividualNeedOtherEntity("", "entity need to be another member")
                        
                        if self.isSameSpecie(entity):
                            self.reproductionChildNumberOnTick += 1
                            
                            return self.reproduction_2_individuals(entity)
                        else:
                            self.reproductionChildNumberOnTick += 1
                            
                            return self.getSpecie().mixDNAandCreatewithOthersSpecies(entity.getSpecie(), self.getDNA(), entity.getDNA())
                    else:
                        raise exceptions.UnknownReproductionType("", "can't reproduce because we don't known type : "+self.reproduction_type)
        return None
    
    def isTimeToDie(self):
        return False
    
    def die(self):
        #si on meurt on indique a notre partenaire que l'on est mort
        if self.partener != None:
            self.partener.reproduction_setPartner(None)
            
    
    def _lifeCycle(self):
        self.internclock += 1
        self.reproductionChildNumberOnTick = 0
    
    def live(self):
        while not self.isTimeToDie():
            self._lifeCycle()