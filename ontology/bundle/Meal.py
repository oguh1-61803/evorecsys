# All necessary libraries and imports from other files.
from src.ontology.item.Food import Food
import copy


# This class represents a meal. A meal consists of a list of side food items and a main food item. The class also
# contains, nutritional data of the meal.
class Meal:

    # Constructor
    def __init__(self, main_food_data, side_food_data_list):

        self.main_food_item = None
        self.side_food_items_list = []
        self.serving_size = 0.0
        self.number_of_calories = 0.0
        self.proteins = 0.0
        self.carbohydrates = 0.0
        self.sugars = 0.0
        self.fiber = 0.0
        self.fats = 0.0
        self.saturated_fats = 0.0
        self.sodium = 0.0

        self.__create_meal(main_food_data, side_food_data_list)

    # This method builds a meal using food items provided as a parameters.
    def __create_meal(self, main_food_data, side_food_data_list):

        self.main_food_item = Food(main_food_data[0], main_food_data[1], main_food_data[2], main_food_data[3],
                                   main_food_data[4], main_food_data[5], main_food_data[6], main_food_data[7],
                                   main_food_data[8], main_food_data[9], main_food_data[10], main_food_data[11],
                                   main_food_data[12], main_food_data[13], main_food_data[14], main_food_data[15],
                                   main_food_data[16])
        self.serving_size += self.main_food_item.serving_size
        self.number_of_calories += self.main_food_item.number_of_calories
        self.proteins += self.main_food_item.protein
        self.carbohydrates += self.main_food_item.carbohydrate
        self.sugars += self.main_food_item.sugar
        self.fiber += self.main_food_item.fiber
        self.fats += self.main_food_item.fat
        self.saturated_fats += self.main_food_item.saturated_fat
        self.sodium += self.main_food_item.sodium

        for side_food_data in side_food_data_list:

            item = Food(side_food_data[0], side_food_data[1], side_food_data[2], side_food_data[3], side_food_data[4],
                        side_food_data[5], side_food_data[6], side_food_data[7], side_food_data[8], side_food_data[9],
                        side_food_data[10], side_food_data[11], side_food_data[12], side_food_data[13],
                        side_food_data[14], side_food_data[15], side_food_data[16])
            self.serving_size += item.serving_size
            self.number_of_calories += item.number_of_calories
            self.proteins += item.protein
            self.carbohydrates += item.carbohydrate
            self.sugars += item.sugar
            self.fiber += item.fiber
            self.fats += item.fat
            self.saturated_fats += item.saturated_fat
            self.sodium += item.sodium

            self.side_food_items_list.append(item)

        self.__normalise_values()

    # This method replaces a main item of a meal. It is used by the evolutionary process.
    def replace_main_item(self, main_item):

        self.serving_size -= self.main_food_item.serving_size
        self.number_of_calories -= self.main_food_item.number_of_calories
        self.proteins -= self.main_food_item.protein
        self.carbohydrates -= self.main_food_item.carbohydrate
        self.sugars -= self.main_food_item.sugar
        self.fiber -= self.main_food_item.fiber
        self.fats -= self.main_food_item.fat
        self.saturated_fats -= self.main_food_item.saturated_fat
        self.sodium -= self.main_food_item.sodium

        reference_calories = copy.deepcopy(self.main_food_item.number_of_calories)
        tailored_serving_size = (reference_calories * main_item.serving_size) / main_item.number_of_calories
        tailored_protein = (reference_calories * main_item.protein) / main_item.number_of_calories
        tailored_carbohydrate = (reference_calories * main_item.carbohydrate) / main_item.number_of_calories
        tailored_sugar = (reference_calories * main_item.sugar) / main_item.number_of_calories
        tailored_fibre = (reference_calories * main_item.fiber) / main_item.number_of_calories
        tailored_fat = (reference_calories * main_item.fat) / main_item.number_of_calories
        tailored_saturated_fat = (reference_calories * main_item.saturated_fat) / main_item.number_of_calories
        tailored_sodium = (reference_calories * main_item.sodium) / main_item.number_of_calories
        self.main_food_item = None
        self.main_food_item = Food(main_item.name, main_item.category, main_item.is_main, main_item.is_breakfast,
                                   main_item.is_lunch, main_item.is_dinner, main_item.is_vegetarian, main_item.is_vegan,
                                   tailored_serving_size, reference_calories, tailored_protein, tailored_carbohydrate,
                                   tailored_sugar, tailored_fibre, tailored_fat, tailored_saturated_fat,
                                   tailored_sodium)
        self.serving_size += tailored_serving_size
        self.number_of_calories += reference_calories
        self.proteins += tailored_protein
        self.carbohydrates += tailored_carbohydrate
        self.sugars += tailored_sugar
        self.fiber += tailored_fibre
        self.fats += tailored_fat
        self.saturated_fats += tailored_saturated_fat
        self.sodium += tailored_sodium

    # This method replaces a side item of a meal by index. It is used by the evolutionary process.
    def replace_side_item(self, side_item, index):

        self.serving_size -= self.side_food_items_list[index].serving_size
        self.number_of_calories -= self.side_food_items_list[index].number_of_calories
        self.proteins -= self.side_food_items_list[index].protein
        self.carbohydrates -= self.side_food_items_list[index].carbohydrate
        self.sugars -= self.side_food_items_list[index].sugar
        self.fiber -= self.side_food_items_list[index].fiber
        self.fats -= self.side_food_items_list[index].fat
        self.saturated_fats -= self.side_food_items_list[index].saturated_fat
        self.sodium -= self.side_food_items_list[index].sodium

        reference_calories = copy.deepcopy(self.side_food_items_list[index].number_of_calories)
        tailored_serving_size = (reference_calories * side_item.serving_size) / side_item.number_of_calories
        tailored_protein = (reference_calories * side_item.protein) / side_item.number_of_calories
        tailored_carbohydrate = (reference_calories * side_item.carbohydrate) / side_item.number_of_calories
        tailored_sugar = (reference_calories * side_item.sugar) / side_item.number_of_calories
        tailored_fibre = (reference_calories * side_item.fiber) / side_item.number_of_calories
        tailored_fat = (reference_calories * side_item.fat) / side_item.number_of_calories
        tailored_saturated_fat = (reference_calories * side_item.saturated_fat) / side_item.number_of_calories
        tailored_sodium = (reference_calories * side_item.sodium) / side_item.number_of_calories
        del self.side_food_items_list[index]
        side_food_item = Food(side_item.name, side_item.category, side_item.is_main, side_item.is_breakfast,
                              side_item.is_lunch, side_item.is_dinner, side_item.is_vegetarian, side_item.is_vegan,
                              tailored_serving_size, reference_calories, tailored_protein, tailored_carbohydrate,
                              tailored_sugar, tailored_fibre, tailored_fat, tailored_saturated_fat, tailored_sodium)
        self.side_food_items_list.insert(index, side_food_item)
        self.serving_size += tailored_serving_size
        self.number_of_calories += reference_calories
        self.proteins += tailored_protein
        self.carbohydrates += tailored_carbohydrate
        self.sugars += tailored_sugar
        self.fiber += tailored_fibre
        self.fats += tailored_fat
        self.saturated_fats += tailored_saturated_fat
        self.sodium += tailored_sodium

    def __normalise_values(self):

        round(self.serving_size, 2)
        round(self.number_of_calories, 2)
        round(self.proteins, 2)
        round(self.carbohydrates, 2)
        round(self.sugars, 2)
        round(self.fiber, 2)
        round(self.fats, 2)
        round(self.saturated_fats, 2)
        round(self.sodium, 2)