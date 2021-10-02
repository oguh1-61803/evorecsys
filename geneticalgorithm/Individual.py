# All necessary libraries and imports from other files.
from src.ontology.bundle.Bundle import Bundle
from src.ontology.bundle.Meal import Meal
from src.ontology.item.PA import PA
import random
import copy


class Individual:

    # These static values act as a reference values when a bundle is built.
    ITEMS_PER_MEAL = 4
    INFERIOR_LIMIT_MAIN_SIZE = 40
    SUPERIOR_LIMIT_MAIN_SIZE = MET_REFERENCE = 60
    MET_TIME_REFERENCE = 60
    CALORIES_CONSTANT = 500

    # These static values represent the index of the list of restrictions
    FOOD_RESTRICTION_INDEX = 0
    SEMANTIC_RESTRICTION_INDEX = 1
    EXERCISING_RESTRICTION_INDEX = 2
    USER_PREFERENCES_RESTRICTION_INDEX = 3

    # Constructor
    def __init__(self, food=None, pas=None, ap=0.0):

        self.food_items = food
        self.pa_items = pas
        self.phenotype = []
        self.aptitude = ap
        self.index = -1

    # This method creates the list of bundles.
    def create_phenotype(self, vegetable_indexes, physical_data):

        for index in range(0, physical_data.number_of_bundles):

            self.__create_bundle(vegetable_indexes, physical_data)

    # This method creates a deep copy of the list of bundles.
    def set_phenotype(self, bundles):

        self.phenotype = []

        for bundle in bundles:

            copy_of_bundle = copy.deepcopy(bundle)
            self.phenotype.append(copy_of_bundle)

    # This method sets the aptidude of the individual
    def set_aptitude(self, aptitude):

        self.aptitude = 0.0
        self.aptitude = aptitude

    # This  method sets the index of the individual
    def set_index(self, index):

        self.index = copy.deepcopy(index)

    # This method evaluates the phenotype using the restrictions.
    def evaluate_phenotype(self, restrictions):

        healthiness_aptitude = restrictions[self.FOOD_RESTRICTION_INDEX].evaluate(self.phenotype)
        consistency_diversity_restriction = restrictions[self.SEMANTIC_RESTRICTION_INDEX].evaluate(self.phenotype)
        exercising_aptitude = restrictions[self.EXERCISING_RESTRICTION_INDEX].evaluate(self.phenotype)
        user_preferences_aptitude = restrictions[self.USER_PREFERENCES_RESTRICTION_INDEX].evaluate(self.phenotype)
        self.aptitude = (healthiness_aptitude + consistency_diversity_restriction + exercising_aptitude +
                         user_preferences_aptitude) / len(restrictions)

    # This method creates a single bundle. It calls other methods to build it.
    def __create_bundle(self, vegetable_indexes, physical_data):

        user_maximum_calories = physical_data.maximum_number_of_calories
        user_weight = physical_data.weight
        user_goal = physical_data.goal
        meal = self.__create_meal(vegetable_indexes, user_maximum_calories)
        pa = self.__create_pa(user_maximum_calories, user_weight, user_goal)
        bundle = Bundle(meal, pa)
        self.phenotype.append(bundle)

    # This method creates a single meal. It uses the tailored calories for the current user.
    def __create_meal(self, vegetable_indexes, user_maximum_calories):

        random_percentage_main_calories = random.randint(self.INFERIOR_LIMIT_MAIN_SIZE, self.SUPERIOR_LIMIT_MAIN_SIZE)
        main_calories = int((user_maximum_calories * random_percentage_main_calories) / 100)
        main_index = random.randrange(len(self.food_items.get("main")))
        reference_main = self.food_items.get("main")[main_index]

        main_serving_size = (main_calories * reference_main.serving_size) / reference_main.number_of_calories
        main_protein = (main_calories * reference_main.protein) / reference_main.number_of_calories
        main_carbohydrate = (main_calories * reference_main.carbohydrate) / reference_main.number_of_calories
        main_sugar = (main_calories * reference_main.sugar) / reference_main.number_of_calories
        main_fiber = (main_calories * reference_main.fiber) / reference_main.number_of_calories
        main_fat = (main_calories * reference_main.fat) / reference_main.number_of_calories
        main_saturated_fat = (main_calories * reference_main.saturated_fat) / reference_main.number_of_calories
        main_sodium = (main_calories * reference_main.sodium) / reference_main.number_of_calories

        main_food_data = (reference_main.name, reference_main.category, reference_main.is_main,
                          reference_main.is_breakfast, reference_main.is_lunch, reference_main.is_dinner,
                          reference_main.is_vegetarian, reference_main.is_vegan, main_serving_size, main_calories,
                          main_protein, main_carbohydrate, main_sugar, main_fiber, main_fat, main_saturated_fat,
                          main_sodium)

        remaining_food_items = self.ITEMS_PER_MEAL - 1
        remaining_calories = user_maximum_calories - main_calories
        calories_per_side_food_item = []
        self.__generate_random_calories(calories_per_side_food_item, remaining_food_items, remaining_calories)

        side_food_data_list = []

        for index in range(0, len(calories_per_side_food_item)):

            if index == 0:

                random_veg_index = random.randrange(len(vegetable_indexes))
                vegetable_index = vegetable_indexes[random_veg_index]
                vegetable_reference = self.food_items.get("side")[vegetable_index]
                vegetable_serving_size = (calories_per_side_food_item[index] * vegetable_reference.serving_size) / \
                                          vegetable_reference.number_of_calories
                vegetable_protein = (calories_per_side_food_item[index] * vegetable_reference.protein) / \
                                     vegetable_reference.number_of_calories
                vegetable_carbohydrate = (calories_per_side_food_item[index] * vegetable_reference.carbohydrate) / \
                                          vegetable_reference.number_of_calories
                vegetable_sugar = (calories_per_side_food_item[index] * vegetable_reference.sugar) / \
                                   vegetable_reference.number_of_calories
                vegetable_fiber = (calories_per_side_food_item[index] * vegetable_reference.fiber) / \
                                    vegetable_reference.number_of_calories
                vegetable_fat = (calories_per_side_food_item[index] * vegetable_reference.fat) / \
                                 vegetable_reference.number_of_calories
                vegetable_saturated_fat = (calories_per_side_food_item[index] * vegetable_reference.saturated_fat) / \
                                           vegetable_reference.number_of_calories
                vegetable_sodium = (calories_per_side_food_item[index] * vegetable_reference.sodium) / \
                                    vegetable_reference.number_of_calories

                vegetable_side_data = (vegetable_reference.name, vegetable_reference.category,
                                       vegetable_reference.is_main, vegetable_reference.is_breakfast,
                                       vegetable_reference.is_lunch, vegetable_reference.is_dinner,
                                       vegetable_reference.is_vegetarian, vegetable_reference.is_vegan,
                                       vegetable_serving_size, calories_per_side_food_item[index], vegetable_protein,
                                       vegetable_carbohydrate, vegetable_sugar, vegetable_fiber, vegetable_fat,
                                       vegetable_saturated_fat, vegetable_sodium)
                side_food_data_list.append(vegetable_side_data)

                continue

            random_side_index = random.randrange(len(self.food_items.get("side")))
            side_reference = self.food_items.get("side")[random_side_index]
            side_serving_size = (calories_per_side_food_item[index] * side_reference.serving_size) / \
                                side_reference.number_of_calories
            side_protein = (calories_per_side_food_item[index] * side_reference.protein) / \
                           side_reference.number_of_calories
            side_carbohydrate = (calories_per_side_food_item[index] * side_reference.carbohydrate) / \
                                side_reference.number_of_calories
            side_sugar = (calories_per_side_food_item[index] * side_reference.sugar) / side_reference.number_of_calories
            side_fiber = (calories_per_side_food_item[index] * side_reference.fiber) / side_reference.number_of_calories
            side_fat = (calories_per_side_food_item[index] * side_reference.fat) / side_reference.number_of_calories
            side_saturated_fat = (calories_per_side_food_item[index] * side_reference.saturated_fat) / \
                                 side_reference.number_of_calories
            side_sodium = (calories_per_side_food_item[index] * side_reference.sodium) / \
                          side_reference.number_of_calories

            side_data = (side_reference.name, side_reference.category, side_reference.is_main,
                         side_reference.is_breakfast, side_reference.is_lunch, side_reference.is_dinner,
                         side_reference.is_vegetarian, side_reference.is_vegan, side_serving_size,
                         calories_per_side_food_item[index], side_protein, side_carbohydrate, side_sugar, side_fiber,
                         side_fat, side_saturated_fat, side_sodium)
            side_food_data_list.append(side_data)

        meal = Meal(main_food_data, side_food_data_list)

        return meal

    # This method creates a single pa. It uses the tailored calories for the current user, their weight and their
    # user goal.
    def __create_pa(self, user_maximum_calories, user_weight, user_goal):

        index = random.randrange(len(self.pa_items))
        pa_reference = self.pa_items[index]
        calories_burned_per_hour = user_weight * pa_reference.met

        if user_goal == 0:

            losing_weight_factor = 0.50
            reference_calories = round(user_maximum_calories * losing_weight_factor)
            calculated_time = round((reference_calories * self.MET_TIME_REFERENCE) / calories_burned_per_hour)
            pa = PA(pa_reference.name, pa_reference.category, pa_reference.indoors, pa_reference.outdoors,
                    pa_reference.intensity, pa_reference.met, calculated_time)

            return pa

        if user_goal == 1:

            maintaining_weight_factor = 0.10
            reference_calories = round(user_maximum_calories * maintaining_weight_factor)
            calculated_time = round((reference_calories * self.MET_TIME_REFERENCE) / calories_burned_per_hour)
            pa = PA(pa_reference.name, pa_reference.category, pa_reference.indoors, pa_reference.outdoors,
                    pa_reference.intensity, pa_reference.met, calculated_time)
            return pa

        if user_goal == 2:

            gaining_weight_factor = 0.10
            reference_calories = round(user_maximum_calories * gaining_weight_factor)
            calculated_time = round((reference_calories * self.MET_TIME_REFERENCE) / calories_burned_per_hour)
            pa = PA(pa_reference.name, pa_reference.category, pa_reference.indoors, pa_reference.outdoors,
                    pa_reference.intensity, pa_reference.met, calculated_time)

            return pa

        if user_goal == 3:

            gaining_muscle_mass = 0.25
            reference_calories = round(user_maximum_calories * gaining_muscle_mass)
            calculated_time = round((reference_calories * self.MET_TIME_REFERENCE) / calories_burned_per_hour)
            pa = PA(pa_reference.name, pa_reference.category, pa_reference.indoors, pa_reference.outdoors,
                    pa_reference.intensity, pa_reference.met, calculated_time)

            return pa

    # This method creates a random number of calories for each food item.
    def __generate_random_calories(self, calories_list, number_of_items, maximum_calories):

        if maximum_calories == 0:

            return True

        remaining_items = number_of_items - 1
        random_calories = random.randint(1, (maximum_calories - remaining_items))
        remaining_calories = maximum_calories - random_calories

        if remaining_items == 0:

            calories_list.append(remaining_calories)

            return True

        elif remaining_items == 1:

            if remaining_calories == 0:

                found = False

                while not found:

                    length = len(calories_list)
                    index = random.randint(0, length - 1)
                    value = calories_list[index]

                    if value < 1:

                        continue

                    calories_list.insert(index, value - 1)
                    found = True

                calories_list.append(1)

                return True

            calories_list.append(random_calories)
            calories_list.append(remaining_calories)

            return True

        else:

            calories_list.append(random_calories)
            return self.__generate_random_calories(calories_list, remaining_items, remaining_calories)
