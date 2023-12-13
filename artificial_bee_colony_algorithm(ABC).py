import random 
import numpy as np

#Função Obejtivo
def objective_function(x):
    return sum(x**2)

def  artificial_bee_colony_algorithm(objective_function, num_variables_vector, num_employed_bees,num_onlooker_bess,num_max_interations):
    
    """
    Função que irá executar o -atificil bee colony algorithm-
    Esta recebe os seguintes parâmetros: 
    
    objetctive_function: Função objetiva que buscamos otimizar
    num_variables_vector : Tamanho do vetor que contêm as soluções. 
    num_employed_bees : numero de abelhas empregadas
    num_onlooker_bees: numero de abelhas observadoras
    mum_max_interactions: numero interações(loop) que irá ocorrer
    """
    
    population = np.random.uniform(low=-10,high=10,size=(num_employed_bees,num_variables_vector))

    #Inicializando solução global
    best_solution = None #vetor com os numeros
    best_fitness = float ('inf') #resultado do somatório
    
    for interations in range(num_max_interations):
        
        #Fase abelhas empregadas
        for c in range(num_employed_bees):
            solution = population[c]
            
            #PERTUBA a solução atual em busca de melhor solução.
            new_solution = solution + np.random.uniform(low=-1, high=1, size=num_variables_vector)
            
            fitness = objective_function(new_solution) #objective_function(função) recebe como parâmetro(new_soluction)
            
            if fitness < objective_function(solution):
                population[c]= new_solution
                
                if fitness < best_fitness:
                    best_solution = new_solution
                    best_fitness = fitness
         
          
        #Fase das abelhas observadoras            
        for c in range(num_onlooker_bess):
            
            solution = random.choice(population)
            
            new_solution = solution + np.random.uniform(low=-1, high=1,size=num_variables_vector)
            
            fitness = objective_function(new_solution) 
            
            
            if fitness < objective_function(solution): #SE o novo "fitness" se mostrar melhor que o atual "fitness", faremos os passos abaixo:
                index = np.where(population == solution)[0][0] #joga o vetor solução para a posição [0][0] da matriz população
                population[index] = new_solution ##Atualiza a população colocondo OUTRO vetor no lugar do vetor solução.

                if fitness < best_fitness:
                    best_solution = new_solution
                    best_fitness = fitness
        
        #Fase das abelhas batedoras(escoteiras), existe para GARANTIR que multiplas possibilidades sejam exploradas.   
        for c in range(num_employed_bees):
            if objective_function(population[c]) >= objective_function(best_solution): #verifica se a aptidão(fitness) da solução atual é maior ou igual à aptidão da melhor solução encontrada até o momento (melhor_solução).
                population[c] = np.random.uniform(low=-10, high=10, size=num_variables_vector) #Se a condição for verdadeira,  o vetor população[i] é 
                #substituído por uma nova solução gerada pela amostragem de valores aleatórios de uma distribuição uniforme dentro do intervalo [-10, 10]
   
    return best_solution, best_fitness         

#Parâmetros
num_variables_vector = 10
num_employed_bees = 20
num_onlooker_bees = 20
max_iterations = 100

#Roda o algorítimo
best_solution, best_fitness = artificial_bee_colony_algorithm(objective_function, num_variables_vector, num_employed_bees, num_onlooker_bees, max_iterations)

#Printa "best_solution" e "best_fitness"
print("Best Solution(vetor_solução):", best_solution)
print()
print("Best Fitness(somatorio_vetor_solução):", best_fitness)
