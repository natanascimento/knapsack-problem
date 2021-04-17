from KnapsackProblem.KnapsackProblem import KnapsackProblem

if __name__ == '__main__':
  max_weight = 200
  length_items = 50
  max_weight_items = 10
  max_price_items = 10
  lenght_population = 100
  lenght_generations = 100
  
  knapsack = KnapsackProblem(max_weight, length_items, max_weight_items, max_price_items, lenght_population, lenght_generations)
  knapsack.solveProblem