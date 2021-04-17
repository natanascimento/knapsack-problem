from KnapsackProblem.KnapsackProblem import KnapsackProblem

if __name__ == '__main__':
  print("------------- Knapsack Informations -------------")
  max_weight = int(input("Select max weight of knapsack: "))
  length_items = int(input("Select max amount of items in the knapsack: "))
  max_weight_items = int(input("Select the max weight of the items in the knapsack: "))
  max_price_items = int(input("Select the maximum value of the items in the knapsack: "))
  lenght_population = int(input("Select population size: "))
  lenght_generations = int(input("Select the number of generations: "))
  
  knapsack = KnapsackProblem(max_weight, length_items, max_weight_items, max_price_items, lenght_population, lenght_generations)
  knapsack.solveProblem