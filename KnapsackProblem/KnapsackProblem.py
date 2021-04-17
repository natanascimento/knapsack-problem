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
  
