# All necessary imports from other files.
from src.ontology.item.Item import Item


# This class instant represents a food item. It contains nutritional data, serving size, if it is vegan/vegetarian,
# if it is main or side, etc. It extends from the Item class.
class Food(Item):

    # Constructor
    def __init__(self, name, category, main, breakfast, lunch, dinner, vegetarian, vegan, size, cal, prot, carbo, sug,
                 fib, fat, sat_fat, sod):

        super().__init__(name, category)

        self.is_main = main
        self.is_breakfast = breakfast
        self.is_lunch = lunch
        self.is_dinner = dinner
        self.is_vegetarian = vegetarian
        self.is_vegan = vegan
        self.serving_size = size
        self.number_of_calories = cal
        self.protein = prot
        self.carbohydrate = carbo
        self.sugar = sug
        self.fiber = fib
        self.fat = fat
        self.saturated_fat = sat_fat
        self.sodium = sod