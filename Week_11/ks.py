from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from copy import deepcopy
from data.ks_data import weights, values, capacity
from charles.selection import fps, tournament
from charles.mutation import binary_mutation, swap_mutation, inversion_mutation
from charles.crossover import single_point_co
from random import random
from operator import attrgetter


def get_fitness(self):
    """A fitness function for the Knapsack Problem.
    Calculates the total values of the elements that are being selected
    if the capacity is not exceeded.
    Otherwise, the fitness value will be proportional to how bad it is.

    Returns:
        int: the total values
    """
    fitness = 0
    weight = 0
    for bit in range(len(self.representation)):
        if self.representation[bit] == 1:
            fitness += values[bit]
            weight += weights[bit]
    if weight > capacity:
        fitness = capacity-weight
    return fitness


def get_neighbours(self):
    """A neighbourhood function for the Knapsack Problem. Flips the bits.

    Returns:
        list: a list of individuals
    """
    n = [deepcopy(self.representation) for i in range(len(self.representation))]

    for count, i in enumerate(n):
        if i[count] == 1:
            i[count] = 0
        elif i[count] == 0:
            i[count] = 1

    n = [Individual(i) for i in n]
    return n


# Monkey Patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

pop = Population(
    size=20, optim="max", sol_size=len(values), valid_set=[0, 1], replacement=True
)

pop.evolve(gens=100,
           select=fps,
           crossover=single_point_co,
           mutate=inversion_mutation,
           co_p=0.9, mu_p=0.1,
           elitism=True)
