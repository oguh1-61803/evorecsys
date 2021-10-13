# All necessary libraries and imports from other files.
from src.geneticalgorithm.Individual import Individual
from src.ontology.bundle.Bundle import Bundle
import random
import copy


# This class represents the population, which consists of a list of individuals. This class controls the genetic
# operators, the selection method, etc.
class Population:

    CROSSOVER_PROBABILITY = 0.6
    MUTATION_PROBABILITY = 0.1
    BUNDLE_CROSSOVER_PROBABILITY = BUNDLE_MUTATION_PROBABILITY = 0.90
    MEAL_PA_PROBABILITY = 0.75
    MAIN_SIDE_PROBABILITY = 0.25
    MANDATORY_SIDE = "vegetable"
    MAIN_REFERENCE = "main"

    # Constructor
    def __init__(self, phys_data, food_pref, pa_pref, food_list, pa_list, individuals, restrictions,
                 mutation_dictionary):

        self.physical_data = phys_data
        self.food_preferences = food_pref
        self.pa_preferences = pa_pref
        self.food_items = food_list
        self.pa_items = pa_list
        self.number_of_individuals = individuals
        self.initial_population = []
        self.intermediate_population = []
        self.best_individual = Individual()
        self.restrictions = restrictions
        self.mutation_dictionary = mutation_dictionary

    # This method creates individuals.
    def create_population(self):

        vegetable_indexes = self.__get_vegetable_indexes()

        for index in range(0, self.number_of_individuals):

            individual = Individual(self.food_items, self.pa_items)
            individual.create_phenotype(vegetable_indexes, self.physical_data)
            self.initial_population.insert(index, individual)

    # This method evaluates individuals employing the restrictions previously built.
    def evaluate_population(self):

        for index in range(0, self.number_of_individuals):

            self.initial_population[index].evaluate_phenotype(self.restrictions)

    # This method finds the best individual. The less aptitude score, the fittest individual is.
    def obtain_best_individual(self):

        aux_average = 0.0
        best_aptitude = 100.00
        best_individual_index = -1

        for index in range(0, self.number_of_individuals):

            aux_average += self.initial_population[index].aptitude

            if self.initial_population[index].aptitude < best_aptitude:

                best_aptitude = self.initial_population[index].aptitude
                best_individual_index = index

        self.best_individual.set_phenotype(self.initial_population[best_individual_index].phenotype)
        self.best_individual.set_aptitude(self.initial_population[best_individual_index].aptitude)
        self.best_individual.set_index(best_individual_index)

    # This method executes the selection method: tournament whose size is 2.
    def execute_tournament(self):

        self.intermediate_population = []
        adversaries = random.sample(range(0, self.number_of_individuals), self.number_of_individuals)

        for index in range(0, self.number_of_individuals):

            if self.initial_population[index].aptitude < self.initial_population[adversaries[index]].aptitude:

                self.intermediate_population.insert(index, self.initial_population[index])

            else:

                self.intermediate_population.insert(index, self.initial_population[adversaries[index]])

    # This method executes the two genetic operators implemented in this system: crossover and mutation.
    def execute_genetic_operators(self):

        if self.mutation_dictionary:

            self.__execute_crossover()
            self.__execute_mutation()

        else:

            self.__execute_crossover()

    # This method copies the new generation of individuals to the original list. It can be understood that an
    # evolutionary cycle has finished.
    def clone_population(self):

        self.initial_population = []
        best_phenotype = self.best_individual.phenotype
        best_individual = Individual()
        best_individual.set_phenotype(best_phenotype)
        self.initial_population.insert(0, best_individual)

        for index in range(1, self.number_of_individuals):

            individual = Individual()
            individual.set_phenotype(self.intermediate_population[index].phenotype)
            self.initial_population.insert(index, individual)

    # This method executes the crossover operator.
    def __execute_crossover(self):

        crossover_aux = random.sample(range(0, self.number_of_individuals), self.number_of_individuals)
        children = []
        crossover_aux_index = 0

        for index in range(0, int(self.number_of_individuals / 2)):

            crossover_probability = random.uniform(0.0, 1.0)

            if crossover_probability < self.CROSSOVER_PROBABILITY:

                mother_index = crossover_aux[index]
                father_index = crossover_aux[index + 1]
                mother = copy.deepcopy(self.intermediate_population[mother_index].phenotype)
                father = copy.deepcopy(self.intermediate_population[father_index].phenotype)
                child_phenotype_1 = []
                child_phenotype_2 = []
                self.__execute_random_combination_of_items(child_phenotype_1, mother, father)
                self.__execute_random_combination_of_items(child_phenotype_2, father, mother)
                child1 = Individual()
                child1.set_phenotype(child_phenotype_1)
                children.insert(crossover_aux_index, child1)
                crossover_aux_index += 1
                child2 = Individual()
                child2.set_phenotype(child_phenotype_2)
                children.insert(crossover_aux_index, child2)
                crossover_aux_index += 1

            else:

                mother_index = crossover_aux[index]
                father_index = crossover_aux[index + 1]
                child1 = Individual()
                child1.set_phenotype(self.intermediate_population[mother_index].phenotype)
                children.insert(crossover_aux_index, child1)
                crossover_aux_index += 1
                child2 = Individual()
                child2.set_phenotype(self.intermediate_population[father_index].phenotype)
                children.insert(crossover_aux_index, child2)
                crossover_aux_index += 1

        for index in range(0, self.number_of_individuals):

            individual = Individual()
            individual.set_phenotype(children[index].phenotype)
            self.intermediate_population[index] = individual

    # This method executes the mutation operator.
    def __execute_mutation(self):

        for index in range(0, self.number_of_individuals):

            mutation_probability = random.uniform(0.0, 1.0)

            if mutation_probability < self.MUTATION_PROBABILITY:
                mutated_individual_phenotype = self.intermediate_population[index].phenotype
                self.__execute_random_swap_of_items(mutated_individual_phenotype)

    # This method is called by the mutation operator.
    def __execute_random_swap_of_items(self, mutated_phenotype, is_cf_individual=False):

        if is_cf_individual:

            mutation_prob = 1.0

        else:

            mutation_prob = self.BUNDLE_MUTATION_PROBABILITY

        for bundle_index in range(0, len(mutated_phenotype)):

            bundle_probability = random.uniform(0.0, 1.0)

            if bundle_probability <= mutation_prob:

                item_list = list(self.mutation_dictionary.keys())
                random_type_index = random.randrange(len(item_list))
                random_type = item_list[random_type_index]
                random_location_list = self.mutation_dictionary.get(random_type)

                if isinstance(random_location_list[0], int):

                    random_index = random.randrange(len(random_location_list))
                    mutated_pa = self.pa_items[random_location_list[random_index]]
                    mutated_phenotype[bundle_index].mutate_pa_item(mutated_pa,
                                                                   self.physical_data.maximum_number_of_calories,
                                                                   self.physical_data.weight, self.physical_data.goal)

                else:

                    random_location_index = random.randrange(len(random_location_list))
                    random_location = random_location_list[random_location_index]
                    mutated_food_item = self.food_items.get(random_location[0])[random_location[1]]

                    if self.MAIN_REFERENCE == random_location[0]:

                        mutated_phenotype[bundle_index].mutate_main_item(mutated_food_item)

                    else:

                        random_index = random.randrange(len(mutated_phenotype[bundle_index].meal.side_food_items_list))
                        mutated_phenotype[bundle_index].mutate_side_item(mutated_food_item, random_index)

    # This method is called by the crossover operator.
    def __execute_random_combination_of_items(self, child_phenotype, receiver, heritage):

        random_bundle_receiver = random.sample(range(0, len(receiver)), len(receiver))
        random_bundle_heritage = random.sample(range(0, len(heritage)), len(heritage))

        for bundle_index in range(0, len(random_bundle_receiver)):

            receiver_bundle = receiver[random_bundle_receiver[bundle_index]]
            heritage_bundle = heritage[random_bundle_heritage[bundle_index]]

            bundle_probability = random.uniform(0.0, 1.0)

            if bundle_probability <= self.BUNDLE_CROSSOVER_PROBABILITY:

                meal_pa_probability = random.uniform(0.0, 1.0)

                if meal_pa_probability <= self.MEAL_PA_PROBABILITY:

                    receiver_meal = receiver_bundle.meal
                    heritage_meal = heritage_bundle.meal

                    main_side_probability = random.uniform(0.0, 1.0)

                    if main_side_probability <= self.MAIN_SIDE_PROBABILITY:

                        child_bundle = Bundle()
                        child_bundle.swap_main_item(receiver_meal, heritage_meal)
                        child_bundle.copy_pa(receiver_bundle.pa)
                        child_phenotype.append(child_bundle)

                    else:

                        random_side_indexes = random.sample(range(0, len(receiver_meal.side_food_items_list)),
                                                            random.randint(1, len(receiver_meal.side_food_items_list)))
                        child_bundle = Bundle()
                        child_bundle.swap_side_items(receiver_meal, heritage_meal, random_side_indexes)
                        child_bundle.copy_pa(receiver_bundle.pa)
                        child_phenotype.append(child_bundle)

                else:

                    heritage_pa = heritage_bundle.pa
                    child_bundle = Bundle()
                    child_bundle.copy_pa(heritage_pa)
                    child_bundle.copy_meal(receiver_bundle.meal)
                    child_phenotype.append(child_bundle)

            else:

                child_bundle = Bundle()
                child_bundle.copy_meal(receiver_bundle.meal)
                child_bundle.copy_pa(receiver_bundle.pa)
                child_phenotype.append(child_bundle)

    def __get_vegetable_indexes(self):

        vegetable_indexes = []
        index = 0

        for side in self.food_items.get("side"):

            if side.category == self.MANDATORY_SIDE:

                vegetable_indexes.append(index)

            index += 1

        return vegetable_indexes
