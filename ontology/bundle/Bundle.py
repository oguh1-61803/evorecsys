# All necessary imports from other files.
from src.ontology.item.PA import PA
from src.ontology.bundle.Meal import Meal


# This class represents a bundle. It contains a physical activity and a meal.
class Bundle:

    # Constructor
    def __init__(self, meal=None, pa=None):

        self.meal: Meal = meal
        self.pa: PA = pa

    # This method copies a meal given as a parameter.
    def copy_meal(self, meal):

        if self.meal is None:

            main_item_data = self.__get_main_food_data(meal)
            side_item_data_list = self.__get_side_food_list_data(meal)
            self.meal = Meal(main_item_data, side_item_data_list)

    # This method copies a physical activity given as a parameter.
    def copy_pa(self, pa):

        if self.pa is None:

            self.pa = PA(pa.name, pa.category, pa.indoors, pa.outdoors, pa.intensity, pa.met, pa.duration)

    # This method swaps the current main food item by a new one given as a parameter. It is used by the crossover
    # genetic operator.
    def swap_main_item(self, receiver_meal, heritage_meal):

        receiver_main_item = receiver_meal.main_food_item
        heritage_main_item = heritage_meal.main_food_item

        mixed_serving_size = (receiver_main_item.number_of_calories * heritage_main_item.serving_size) / \
                              heritage_main_item.number_of_calories
        mixed_protein = (receiver_main_item.number_of_calories * heritage_main_item.protein) / \
                         heritage_main_item.number_of_calories
        mixed_carbohydrate = (receiver_main_item.number_of_calories * heritage_main_item.carbohydrate) / \
                              heritage_main_item.number_of_calories
        mixed_sugar = (receiver_main_item.number_of_calories * heritage_main_item.sugar) / \
                             heritage_main_item.number_of_calories
        mixed_fiber = (receiver_main_item.number_of_calories * heritage_main_item.fiber) / \
                      heritage_main_item.number_of_calories
        mixed_fat = (receiver_main_item.number_of_calories * heritage_main_item.fat) / \
                      heritage_main_item.number_of_calories
        mixed_saturated_fat = (receiver_main_item.number_of_calories * heritage_main_item.saturated_fat) / \
                      heritage_main_item.number_of_calories
        mixed_sodium = (receiver_main_item.number_of_calories * heritage_main_item.sodium) / \
                      heritage_main_item.number_of_calories

        mixed_main_item = (heritage_main_item.name, heritage_main_item.category, heritage_main_item.is_main,
                           heritage_main_item.is_breakfast, heritage_main_item.is_lunch, heritage_main_item.is_dinner,
                           heritage_main_item.is_vegetarian, heritage_main_item.is_vegan, mixed_serving_size,
                           receiver_main_item.number_of_calories, mixed_protein, mixed_carbohydrate, mixed_sugar,
                           mixed_fiber, mixed_fat, mixed_saturated_fat, mixed_sodium)

        receiver_side_food_item_list = self.__get_side_food_list_data(receiver_meal)
        self.meal = Meal(mixed_main_item, receiver_side_food_item_list)

    # This method swaps at least one of the current side food items by new ones given as a parameter. It is used by
    # the crossover genetic operator.
    def swap_side_items(self, receiver_meal, heritage_meal, side_indexes):

        list_of_mixed_side_items = []

        for index in range(0, len(receiver_meal.side_food_items_list)):

            if index in side_indexes:

                receiver_side_item = receiver_meal.side_food_items_list[index]
                heritage_side_item = heritage_meal.side_food_items_list[index]

                mixed_serving_size = (receiver_side_item.number_of_calories * heritage_side_item.serving_size) / \
                                     heritage_side_item.number_of_calories
                mixed_protein = (receiver_side_item.number_of_calories * heritage_side_item.protein) / \
                                heritage_side_item.number_of_calories
                mixed_carbohydrate = (receiver_side_item.number_of_calories * heritage_side_item.carbohydrate) / \
                                     heritage_side_item.number_of_calories
                mixed_sugar = (receiver_side_item.number_of_calories * heritage_side_item.sugar) / \
                              heritage_side_item.number_of_calories
                mixed_fiber = (receiver_side_item.number_of_calories * heritage_side_item.fiber) / \
                              heritage_side_item.number_of_calories
                mixed_fat = (receiver_side_item.number_of_calories * heritage_side_item.fat) / \
                            heritage_side_item.number_of_calories
                mixed_saturated_fat = (receiver_side_item.number_of_calories * heritage_side_item.saturated_fat) / \
                                      heritage_side_item.number_of_calories
                mixed_sodium = (receiver_side_item.number_of_calories * heritage_side_item.sodium) / \
                               heritage_side_item.number_of_calories

                mixed_side_item = (heritage_side_item.name, heritage_side_item.category, heritage_side_item.is_main,
                                   heritage_side_item.is_breakfast, heritage_side_item.is_lunch,
                                   heritage_side_item.is_dinner, heritage_side_item.is_vegetarian,
                                   heritage_side_item.is_vegan, mixed_serving_size,
                                   receiver_side_item.number_of_calories, mixed_protein, mixed_carbohydrate,
                                   mixed_sugar, mixed_fiber, mixed_fat, mixed_saturated_fat, mixed_sodium)
                list_of_mixed_side_items.append(mixed_side_item)

            else:

                receiver_side_item = receiver_meal.side_food_items_list[index]

                not_mixed_side_item = (receiver_side_item.name, receiver_side_item.category, receiver_side_item.is_main,
                                       receiver_side_item.is_breakfast, receiver_side_item.is_lunch,
                                       receiver_side_item.is_dinner, receiver_side_item.is_vegetarian,
                                       receiver_side_item.is_vegan, receiver_side_item.serving_size,
                                       receiver_side_item.number_of_calories, receiver_side_item.protein,
                                       receiver_side_item.carbohydrate, receiver_side_item.sugar,
                                       receiver_side_item.fiber, receiver_side_item.fat,
                                       receiver_side_item.saturated_fat, receiver_side_item.sodium)
                list_of_mixed_side_items.append(not_mixed_side_item)

        receiver_main_item = self.__get_main_food_data(receiver_meal)
        self.meal = Meal(receiver_main_item, list_of_mixed_side_items)

    # This method replaces the main item of the meal. It is used by te mutation genetic operator.
    def mutate_main_item(self, main_item):

        self.meal.replace_main_item(main_item)

    # This method replaces the side items of the meal by index. It is used by te mutation genetic operator.
    def mutate_side_item(self, side_item, random_index):

        self.meal.replace_side_item(side_item, random_index)

    # This method replaces the physical activity of the bundle. It is used by te mutation genetic operator.
    def mutate_pa_item(self, pa_item, user_maximum_calories, user_weight, user_goal):

        calories_burned_per_hour = user_weight * pa_item.met
        met_time_reference = 60.0

        if user_goal == 0:

            losing_weight_factor = 0.50
            reference_calories = round(user_maximum_calories * losing_weight_factor)
            calculated_time = round((reference_calories * met_time_reference) / calories_burned_per_hour)
            self.pa = None
            self.pa = PA(pa_item.name, pa_item.category, pa_item.indoors, pa_item.outdoors, pa_item.intensity,
                         pa_item.met, calculated_time)

        if user_goal == 1:

            maintaining_weight_factor = 0.10
            reference_calories = round(user_maximum_calories * maintaining_weight_factor)
            calculated_time = round((reference_calories * met_time_reference) / calories_burned_per_hour)
            self.pa = None
            self.pa = PA(pa_item.name, pa_item.category, pa_item.indoors, pa_item.outdoors, pa_item.intensity,
                         pa_item.met, calculated_time)

        if user_goal == 2:

            gaining_weight_factor = 0.10
            reference_calories = round(user_maximum_calories * gaining_weight_factor)
            calculated_time = round((reference_calories * met_time_reference) / calories_burned_per_hour)
            self.pa = None
            self.pa = PA(pa_item.name, pa_item.category, pa_item.indoors, pa_item.outdoors, pa_item.intensity,
                         pa_item.met, calculated_time)

        if user_goal == 3:

            gaining_muscle_mass = 0.25
            reference_calories = round(user_maximum_calories * gaining_muscle_mass)
            calculated_time = round((reference_calories * met_time_reference) / calories_burned_per_hour)
            self.pa = None
            self.pa = PA(pa_item.name, pa_item.category, pa_item.indoors, pa_item.outdoors, pa_item.intensity,
                         pa_item.met, calculated_time)

    def __get_main_food_data(self, meal):

        main_item_data = (meal.main_food_item.name, meal.main_food_item.category, meal.main_food_item.is_main,
                          meal.main_food_item.is_breakfast, meal.main_food_item.is_lunch,
                          meal.main_food_item.is_dinner, meal.main_food_item.is_vegetarian,
                          meal.main_food_item.is_vegan, meal.main_food_item.serving_size,
                          meal.main_food_item.number_of_calories, meal.main_food_item.protein,
                          meal.main_food_item.carbohydrate, meal.main_food_item.sugar, meal.main_food_item.fiber,
                          meal.main_food_item.fat, meal.main_food_item.saturated_fat, meal.main_food_item.sodium)

        return main_item_data

    def __get_side_food_list_data(self, meal):

        side_item_data_list = []

        for side_item in meal.side_food_items_list:

            side_item_data = (side_item.name, side_item.category, side_item.is_main, side_item.is_breakfast,
                              side_item.is_lunch, side_item.is_dinner, side_item.is_vegetarian, side_item.is_vegan,
                              side_item.serving_size, side_item.number_of_calories, side_item.protein,
                              side_item.carbohydrate, side_item.sugar, side_item.fiber, side_item.fat,
                              side_item.saturated_fat, side_item.sodium)
            side_item_data_list.append(side_item_data)

        return side_item_data_list
