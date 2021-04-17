import random
from deap import algorithms as alg, base, creator, tools

class KnapsackProblem:
  
  def __init__(self, max_weight, length_items, max_weight_items, max_price_items, lenght_population, lenght_generations):
    self.max_weight = max_weight
    self.length_items = length_items
    self.max_weight_items = max_weight_items
    self.max_price_items = max_price_items
    self.lenght_population = lenght_population
    self.lenght_generations = lenght_generations
    self.items = []
    self.population = []
    self.toolbox = base.Toolbox()
    self.best_option = 0
    
  @property 
  def createItems(self):
    for i in range(self.length_items):
      self.items.append({"weight": random.randint(1, self.max_weight_items), 
                         "value": random.randint(1, self.max_price_items)})
    return self.items
  
  def setFitness(self, individual):
    weight = 0
    value = 0
    for index, item in enumerate(individual):
        if item == 1:
            weight += self.items[index]['weight']
            value += self.items[index]['value']
    if weight > self.max_weight:
        return 0,
    return value,
  
  @property
  def setToolbox(self):
    creator.create("Fitness", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.Fitness)
    self.toolbox.register("attr_bool", random.randint, 0, 1)
    self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr_bool, n=self.length_items)
    self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual, n=self.lenght_generations)
    
    self.population = self.toolbox.population()
    
    self.toolbox.register("evaluate", self.setFitness)
    self.toolbox.register("mate", tools.cxTwoPoint)
    self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    self.toolbox.register("select", tools.selTournament, tournsize=3)
  
  @property
  def setGenerations(self):
    for gen in range(self.lenght_generations):
      offspring = alg.varAnd(self.population, self.toolbox, cxpb=0.5, mutpb=0.1)
      fits = self.toolbox.map(self.toolbox.evaluate, offspring)
      for fit, ind in zip(fits, offspring):
          ind.fitness.values = fit
      self.population = self.toolbox.select(offspring, k=len(self.population))
  
  @property
  def bestOption(self):
    bests = tools.selBest(self.population, k=10)
    self.best_option = bests[0]
    return self.best_option
  
  @property
  def showItems(self):
    print("\n------------ Items ------------")
    for item in self.items:
      print(item)
      
  @property
  def getKnapsackMaxWeight(self):
    print("Max Capacity of this Knapsack: {}kg".format(self.max_weight))
    
  @property
  def show(self):
    print("\n------------ Result ------------")
    weight = 0
    value = 0
    for index, item in enumerate(self.best_option):
        if item == 1:
            print(self.items[index])
            weight += self.items[index]['weight']
            value += self.items[index]['value']

    print('\nTotal Weight: {}kg'.format(weight))
    print('Total Value: ${}'.format(value))
      
  @property
  def solveProblem(self):
    self.getKnapsackMaxWeight
    self.createItems
    self.showItems
    self.setToolbox
    self.setGenerations
    self.bestOption
    self.show