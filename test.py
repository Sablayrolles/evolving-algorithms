# -*- coding: utf-8 -*-
"""
Genetic Algorithm :
    
1. Create the population

2. Determine fitness

3. Select the mating pool

4. Breed

5. Mutate

6. Repeat

"""

""" to do : 
    create a set of species
    create for each specie a class of own fitness herited from Fitness class
    create a population
    
    for n generation :
        generate a generation
        run the generation
        select a part of generation
            -> order the generation
               -> calculate fitness of each Entity
        breed new a new generation
        apply some mutation on the new generation
"""
""" 
    Exceptions
    
    def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")

class InputError(Error):
    # Exception raised for errors in the input.
    # Attributes:
    #     expression -- input expression in which the error occurred
    #     message -- explanation of the error

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
"""

# TO DO : add check type of object ->
# instance.__class__.__mro__ => liste des classes de la plus specifique à la plus générale (object)
#si class MyEntity(Entity):
#       pass
#
# m = MyEntity(1)
#m.__class__.__mro__ => (__main__.myEntity, __main__.Entity, object)

# TO DO : neural networks
# genetics algorithms with 4 parameters to tune ::
#   - number of layers (network_depth)
#   - number of neurons per layer (network_width)
#   - dense layer activation function
#   - network optimizer
#
#   => mixDNA on prend la valeur de chaque paramètres au hasard (random.choice[]) entre les deux parents

# TO DO : Continuous Evoutionary System
#
# les entités peuvent choisir l'action de se reproduire 
# - fitness => maxlife (plus il vit longtemps mieux c'est :: max fitness)
# - chance die mechanism => select 
# - breed => action to reproduce


class Fitness:
    def __init__(self):
        pass
    
    def entity_fitness(self, entity):
        pass
    
    def compare_fitness(self, entity1, entity2):
        pass
    
class Specie:
    nbCreated = 0
    def __init__(self, fitness, name=""):
        self.nbCreated += 1
        
        self.id = self.nbCreated
        self.name = name
        self.fitness = fitness
    
    def getId(self):
        return self.id
    
    def equals(self, specie):
        return self.id == specie.getId()
    
    def compatibiliy(self, specie):
        pass
    
    def mixDNA(DNA1, DNA2):
        #mix the 2 DNA and return a new DNA
        pass
    
class Entity:
    nbCreated = 0
    def __init__(self, specie, reproduction_type="clone", reproduction_max_child=0): 
        # reproduction_type = ["clone", "replicated", "couple", "binary"]
        # clone: the individual make a copy of itself younger
        # replicated : the indicidual make a copy of itself
        # couple : the individual can reproduce only with a single entity only once (sameAsOldGeneration if not died)
        # binary : the individual can reproduce with any entity only once
        
        #reproduction_max_child = 0 : no limit
        self.nbCreated += 1
        
        self.id = self.nbCreated
        self.specie = specie
        self.reproduction_type = reproduction_type
        self.reproduction_max_child = reproduction_max_child
        self.partener = None
        
        self.reproductionChildNumberOnTick = 0
        self.interclock = 0
        
    def getId(self):
        return self.id
    
    def equals(self, entity):
        return self.id == entity.getId()
    
    def getSpecie(self):
        return self.specie
    
    def getDNA(self):
        return self.__dict__
    
    def clone(self, reinitialiseInternalClock = True):
        DNA = self.getDNA()
        
        if reinitialiseInternalClock:
            DNA["interclock"] = 0
            
        return DNA
    
    def injectDNA(self, DNA, keepSameId = False):
        if not keepSameId:
            id_save = self.id
        self.__dict__ = DNA
        if not keepSameId:
            self.id = id_save
    
    def randomParameters(specie):
        return Entity(specie)
    
    def fitness(self):
        return self.specie.entity_fitness(self)
    
    def reproduction_setPartner(self, entity):
        self.partener = entity
        
    def checkIfReproductionIsPossible(self, entity):
        #to complete with test of sex parameters for exemple
        return True
    
    def reproduction_2_individuals(self, entity):
        if self.checkIfReproductionIsPossible(entity):
            return Entity(entity.getSpecie())
        else:
            return None
    
    def reproduce(self, entity=None):
        newEntity = Entity(self.specie)
        
        self.reproductionChildNumberOnTick += 1
        
        if self.reproduction_type == "clone" and (self.reproduction_max_child == 0 or self.reproductionChildNumberOnTick < self.reproduction_max_child):
            #on check le nombre d'enfant
            newEntity.injectDNA(self.clone())
        else:
            if self.reproduction_type == "replicated" and (self.reproduction_max_child < -1 or self.reproductionChildNumberOnTick < self.reproduction_max_child):
                newEntity.injectDNA(self.clone(reinitialiseInternalClock = False))
            else:
                if self.reproduction_type == "couple" and (self.reproduction_max_child < -1 or self.reproductionChildNumberOnTick < self.reproduction_max_child):
                    
                    #si le couple n'est pas créé on le créé:
                    if self.partener == None:
                        self.partener = entity
                        #et on créé la réplique chez le partener
                        entity.reproduction_setPartner(self)
                    
                    if entity.equals(self.partener) and entity != None:
                        return self.reproduction_2_individuals(entity)
                else:
                    if self.reproduction_type == "binary" and (self.reproduction_max_child < -1 or self.reproductionChildNumberOnTick < self.reproduction_max_child):
                        if entity != None:
                            return self.reproduction_2_individuals(entity)
                    else:
                        pass
                        #raise Unknown reproduction type
    
    def isTimeToDie(self):
        pass
    
    def die(self):
        #si on meurt on indique a notre partenaire que l'on est mort
        if self.partener != None:
            self.partener.reproduction_setPartner(None)
            
    
    def _lifeCycle(self):
        self.interclock += 1
        self.reproductionChildNumberOnTick = 0
    
    def live(self):
        pass

class Environnement:
    def __init__(self):
        pass
    
    def tick(self):
        pass
    
class Population:
    nbCreated = 0
    num_gen_act = 0
    
    def __init__(self, size, percent_selection, chance_mutation, species, species_repartition, name="", nb_thread=1):
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
        pass
    
class Statistique:
    def __init__(self, population):
        self.targetPopulation = population
        
    def getInformations(self, population):
        return [self.targetPopulation.getEntitiesFitness(),  self.targetPopulation.getEntitiesDictionnaries()]
    
    
class World:
    def __init__(self, environnement, populations_list, name = ""):
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
        
        
if __name__ == "__main__":
    pass