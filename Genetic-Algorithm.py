import random


def fitness(x):
    return x ** 2


def binary_to_int(binary):
    return int(binary, 2)


def generate_population(size):
    return ["".join(random.choice("01") for _ in range(4)) for _ in range(size)]


def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    selected = random.choices(population, weights=probabilities, k=2)
    return selected


def crossover(parent1, parent2):
    point = random.randint(1, 3)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def mutate(binary, mutation_rate=0.1):
    binary = list(binary)
    for i in range(len(binary)):
        if random.random() < mutation_rate:
            binary[i] = "0" if binary[i] == "1" else "1"
    return "".join(binary)


def genetic_algorithm(generations=5, population_size=4):
    population = generate_population(population_size)
    for generation in range(generations):
        print(f"Generation {generation+1}: {population}")
        fitness_values = [fitness(binary_to_int(ind)) for ind in population]
        
        
        parent1, parent2 = roulette_wheel_selection(population, fitness_values)
        
       
        child1, child2 = crossover(parent1, parent2)
        
        
        child1 = mutate(child1)
        child2 = mutate(child2)
        
        
        population = [child1, child2] + random.sample(population, 2)  # Keep two random individuals
    
    
    best_solution = max(population, key=lambda x: fitness(binary_to_int(x)))
    best_x = binary_to_int(best_solution)
    print(f"Best solution found: x = {best_x}, f(x) = {fitness(best_x)}")


genetic_algorithm()
