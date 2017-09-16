'''
    File name: Hello_World_Genetic_Algorithm.py
    Author: David Jura
    Date created: 9/16/17
    Python Version: 3.5.2
'''
import random, operator

##Calculate fitness of a string when compared to 'helloworld'
def calcFitness(speciman):
    comparison = "helloworld";
    fitness = 0;
    for i in range(len(speciman)):
        if(speciman[i] == comparison[i]):
            fitness += 10;
    return fitness;

##Generate a random population
def generateRandomPopulation():
    population = {};
    for i in range(30):
        randSpeciman = "";
        for x in range(10):
            randSpeciman += chr(random.randint(97,122));
        population[randSpeciman] = calcFitness(randSpeciman);
    return population;

##Get the top 3 most fit strings in the population
def getTopFit(pop):
    largest = {}

    currentLargeValue = list(pop.keys())[0]
    currentLarge = pop[list(pop.keys())[0]]
    for i in range(3):
        currentLargeValue = list(pop.keys())[0]
        currentLarge = pop[list(pop.keys())[0]]
        for key in pop.keys():
            if(pop[key] > currentLarge):
                currentLarge = pop[key];
                currentLargeValue = key;
        largest[currentLargeValue] = currentLarge
        del pop[currentLargeValue]
    return largest

##Perform uniform crossover with 0.83% mutation rate
def crossover(largest):
    newPopulation = {}
    index = 0
    while len(list(newPopulation)) < 30:
        if(index == 2):
            parent1 = list( largest.keys() )[index];
            parent2 = list( largest.keys() )[0];
            child = "";
            for i in range(len(parent1)):
                mutationRate = random.randint(1,120);
                if(mutationRate == 1):
                    child += chr(random.randint(97,122));
                else:
                    probability = random.randint(1,2);
                    if(probability == 1):
                        child += parent1[i];
                    else:
                        child += parent2[i];
            newPopulation[child] = calcFitness(child);
                
            index = 0;
        else:
            parent1 = list( largest.keys() )[index];
            parent2 = list( largest.keys() )[index+1];
            child = "";
            for i in range(len(parent1)):
                mutationRate = random.randint(1,120);
                if(mutationRate == 1):
                    child += chr(random.randint(97,122));
                else:
                    probability = random.randint(1,4);
                    if(probability == 1):
                        child += parent1[i];
                    else:
                        child += parent2[i];
            newPopulation[child] = calcFitness(child);
            index += 1;
            
    return newPopulation;

##main function
def main():
    population = generateRandomPopulation();
    generations = int(input("How many generations would you like to iterate through?"))
    for i in range(generations):
        largest = getTopFit(population)
        population = crossover(largest);
        print("generation " + str(i+1) + " - Most fit: " + str( list(largest.keys())[2]))
    print("\n---Last Generation population--")
    for i in list(population.keys()):
        print("String: " + i + ", Fitness: " + str(population[i]))
    print("--------------------------------")

##Run main function
if __name__ == "__main__":
    main()
