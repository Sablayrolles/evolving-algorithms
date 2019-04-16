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

# TO DO : graphic interface
# pygame

# TO DO : neural networks
# genetics algorithms with 4 parameters to tune ::
#   - number of layers (network_depth)
#   - number of neurons per layer (network_width)
#   - dense layer activation function
#   - network optimizer
#
#   => mixDNA:
#   on ajoute a mixDNA(percentDropOut):
#   - listIn \cup listIn \minus dropOut
#   - listOut \cup listOut \minus dropOut
#   - nbCouches \mean nbCouches -1 couche dropOut
#   - dimCouches[i] \mean dimCouches[i] +- dropOut
#   - activationCouches[i] choice activationCouches[i]
#   - optimisation choice optimisation

# TO DO : Continuous Evoutionary System
#
# les entités peuvent choisir l'action de se reproduire 
# - fitness => maxlife (plus il vit longtemps mieux c'est :: max fitness)
# - chance die mechanism => select 
# - breed => action to reproduce