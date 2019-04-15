# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 00:31:19 2019

@author: Megaport
"""

""" to do : 
    V 1) create for each specie you want a class of own fitness herited from Fitness class
    V 2) create a set of species herited from Specie class
    V 3) create a set of Entities class for each specie herited from Entity class
    V 4) craete environnements
    V 5) create a population herited from Population class for your set of entities class and species
    V 6) create a statistique class for the analysis of a population
    V 7) create a world class to run the test
    V 8) create a main to run the application 
"""
import random
import numpy
import statistics
from pprint import pprint
import matplotlib.pyplot as plt

import evolving

class NotANumberSpeed(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

#fitness 1)
class FitnessBlock(evolving.fitness.Fitness):
    def entity_fitness(self, entity):
        super().entity_fitness(entity)
        
        return entity.getPosX()
    
    def compare_fitness(self, entity1, entity2):
        super().compare_fitness(entity1, entity2)
        
        if self.entity_fitness(entity1) < self.entity_fitness(entity2):
            return -1
        else:
            if self.entity_fitness(entity1) == self.entity_fitness(entity2):
                return 0
            else:
                return -1
f = FitnessBlock()

"""
---------------------
"""
     
#species 2)
class Blocs(evolving.specie.Specie):
    def __init__(self, fitness, name=""):
        super().__init__(fitness, name=name)
s = Blocs(f, "Blocs")

"""
---------------------
"""
   
#entity class 3)
class BlocEntity(evolving.entity.Entity):
    def __init__(self, specie, speed):
        super().__init__(specie, reproduction_type="clone", reproduction_max_child=-1)
        
        if str(type(speed)) != "<class 'int'>" and str(type(speed)) != "<class 'float'>":
            print(str(type(speed)))
            raise NotANumberSpeed("", "speed need to be an int or a float")
            
        self.speed = speed
        
        self.posX = 0
        self.maxTime = 100
        
    def __str__(self):
        return "BlocEntity(#"+str(self.id)+", posX="+str(self.posX)+", speed="+str(self.speed)+", internclock="+str(self.internclock)+")"
    
    def __repr__(self):
        return self.__str__()
    
    def randomParameters(specie):
        return BlocEntity(specie, random.randint(-10,10))
    
    def _initialize(self):
        self.posX = 0
        
    def mixDNA(self, DNA1, DNA2):
        super().mixDNA(DNA1, DNA2)
        
        newDNA = DNA1.copy()
        newDNA["speed"] = (DNA1["speed"] + DNA2["speed"]) / 2.
        
        return newDNA
    
    
    def mutate(self, percent_mutation):
        self.speed = float(self.speed) + float(random.choice([-1,1]))*percent_mutation*float(self.speed)
    
    def reproduction_2_individuals(self, entity):
        super().reproduction_2_individuals(entity)
        
        newEntity = self.__class__.randomParameters(self.getSpecie())
        
        newEntity.injectDNA(self.mixDNA(self.getDNA(), entity.getDNA()), keepSameId=False)
        newEntity._initialize()
        
        return newEntity
            
    def reproduce(self, entity=None, keepSameId=False):
        e = super().reproduce(entity=entity, keepSameId=keepSameId)
        if self.reproduction_type != "replicated":
            e._initialize()
        
        return e
        
    def getPosX(self):
        return self.posX
    
    def move(self):
        self.posX += self.speed
        
    def isTimeToDie(self):
        return self.internclock > self.maxTime
    
    def _lifeCycle(self):
        super()._lifeCycle()
        
        self.move()
        
    def live(self):
        while not self.isTimeToDie():
            self._lifeCycle()
            
e = BlocEntity(s, 0.2)
e2 = BlocEntity(s, -0.5)
e3 = BlocEntity(s, 0.3)

"""
#for couple and multiple => ok
e_1 = e.reproduce(e2)
e_2 = e.reproduce(e3)

# for clone & replicated ==> ok
e.live()
e_1 = e.reproduce(keepSameId=True)
"""
        
"""
---------------------
"""

#environnement 4)
env = evolving.environnement.Environnement()

"""
---------------------
"""

#population class 5)

class BlockPopulation(evolving.population.Population):
    def runGeneration(self, environnement):
        for e in self.actualGen:
            e.live()
            
    def orderGeneration(self):
        order = {}
        
        for e in self.actualGen:
            order[e] = e.fitness()

        neworder = {k:v for k,v in sorted(order.items(), key=lambda x: -x[1])}
        
        self.order = neworder
    
    def selectGeneration(self):
        nbEnt = int(self.percent_selection*self.size)
    
        for i in range(nbEnt):
            self.selectGen.append(list(self.order.keys())[i])
            
    def breedGeneration(self):
        self.nextGen = []
        
        probability_of_select = [1.0/float(len(self.selectGen)) for _ in range(len(self.selectGen))]

        
        #self.size : nbItems to pick if we want couple : self.size*self.size
        mono_parent_list = numpy.random.choice(self.selectGen, self.size, p=probability_of_select)
        
        for p in mono_parent_list:
            self.nextGen.append(p.reproduce())
            
    def mutateGeneration(self):
        for e in self.nextGen:
            if random.random() < self.chance_mutation:
                e.mutate(self.percent_variation_mutation)
    
p = BlockPopulation(size=10, percent_selection=0.7, chance_mutation=0.3, percent_variation_mutation=0.2, species_caracteristiques= [{"class": BlocEntity, "specie": s, "percent": 1}])
#p.createGeneration()
#p.runGeneration(env)
#p.orderGeneration()
#p.selectGeneration()
#p.breedGeneration()
#p.mutateGeneration()

"""
---------------------
"""

#statistique class 6)
class BlockStatistiques(evolving.statistique.Statistique):
    pass

stat = BlockStatistiques(p)
#stat.fetchInformationsGeneration()

"""
---------------------
"""

#world class 7)
w = evolving.world.World(env, [p], {p: stat}, "Blockworld")
"""
w.tick()
print(w.getStatistiquesDict()[p].getAllInformations())
"""

"""
---------------------
"""

#main 8)
w.run(10000)
fitnessGen = {data["gennum"] : data["fitness"] for data in w.getStatistiquesDict()[p].getAllInformations()}
statFitness = {num : {"min": min(f), "max": max(f), "median": statistics.median(f), "mean": statistics.mean(f)} for num, f in fitnessGen.items()}
pprint(statFitness)


plt.plot(statFitness.keys(), [v["min"] for k,v in statFitness.items()], 'ro--', label="min")
plt.plot(statFitness.keys(), [v["max"] for k,v in statFitness.items()], 'bs--', label="max")
plt.plot(statFitness.keys(), [v["median"] for k,v in statFitness.items()], 'g^--', label="median")
plt.plot(statFitness.keys(), [v["mean"] for k,v in statFitness.items()], 'm+--', label="mean")
plt.xlabel('Num generation')
plt.ylabel('fitness')
plt.legend()
plt.show()
