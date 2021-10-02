# This class represents the food preferences of the current user.
class FoodPreferenceData:

    # Constructor
    def __init__(self, bread, cereal, dairy, egg, fish, fruit, grain, legume, meat, nut, pasta, poultry, seafood,
                 vegetable):

        self.bread_value = bread
        self.cereal_value = cereal
        self.dairy_value = dairy
        self.egg_value = egg
        self.fish_value = fish
        self.fruit_value = fruit
        self.grain_value = grain
        self.legume_value = legume
        self.meat_value = meat
        self.nut_value = nut
        self.pasta_value = pasta
        self.poultry_value = poultry
        self.seafood_value = seafood
        self.vegetable_value = vegetable

    # This method gets the values associated to the preference of each food category.
    def get_selected_values(self, limit):

        type_list = []

        if self.bread_value >= limit:

            type_list.append('bread')

        if self.cereal_value >= limit:

            type_list.append('cereal')

        if self.dairy_value >= limit:

            type_list.append('dairy')

        if self.egg_value >= limit:

            type_list.append('egg')

        if self.fish_value >= limit:

            type_list.append('fish')

        if self.fruit_value >= limit:

            type_list.append('fruit')

        if self.grain_value >= limit:

            type_list.append('grain')

        if self.legume_value >= limit:

            type_list.append('legume')

        if self.meat_value >= limit:

            type_list.append('meat')

        if self.nut_value >= limit:

            type_list.append('nut')

        if self.pasta_value >= limit:

            type_list.append('pasta')

        if self.poultry_value >= limit:

            type_list.append('poultry')

        if self.seafood_value >= limit:

            type_list.append('seafood')

        if self.vegetable_value >= limit:

            type_list.append('vegetable')

        return type_list

    # This method gets the highest evaluated types of food by the user.
    def get_higher_evaluated_types(self):

        dictionary_of_best_types = {}
        first_list_of_best_types = []
        second_list_of_best_types = []
        list_of_values = [self.bread_value, self.cereal_value, self.dairy_value,  self.egg_value, self.fish_value,
                          self.fruit_value,  self.grain_value, self.legume_value, self.meat_value, self.nut_value,
                          self.pasta_value, self.poultry_value, self.seafood_value, self.vegetable_value]
        maximum_value = max(list_of_values)
        second_maximum_value = maximum_value - 1

        if self.bread_value == maximum_value:

            first_list_of_best_types.append('bread')

        else:

            if self.bread_value == second_maximum_value:

                second_list_of_best_types.append('bread')

        if self.cereal_value == maximum_value:

            first_list_of_best_types.append('cereal')

        else:

            if self.cereal_value == second_maximum_value:

                second_list_of_best_types.append('cereal')

        if self.dairy_value == maximum_value:

            first_list_of_best_types.append('dairy')

        else:

            if self.dairy_value == second_maximum_value:

                second_list_of_best_types.append('dairy')

        if self.egg_value == maximum_value:

            first_list_of_best_types.append('egg')

        else:

            if self.egg_value == second_maximum_value:

                second_list_of_best_types.append('egg')

        if self.fish_value == maximum_value:

            first_list_of_best_types.append('fish')

        else:

            if self.fish_value == second_maximum_value:

                second_list_of_best_types.append('fish')

        if self.fruit_value == maximum_value:

            first_list_of_best_types.append('fruit')

        else:

            if self.fruit_value == second_maximum_value:

                second_list_of_best_types.append('fruit')

        if self.grain_value == maximum_value:

            first_list_of_best_types.append('grain')

        else:

            if self.grain_value == second_maximum_value:

                second_list_of_best_types.append('grain')

        if self.legume_value == maximum_value:

            first_list_of_best_types.append('legume')

        else:

            if self.legume_value == second_maximum_value:

                second_list_of_best_types.append('legume')

        if self.meat_value == maximum_value:

            first_list_of_best_types.append('meat')

        else:

            if self.meat_value == second_maximum_value:

                second_list_of_best_types.append('meat')

        if self.nut_value == maximum_value:

            first_list_of_best_types.append('nut')

        else:

            if self.nut_value == second_maximum_value:

                second_list_of_best_types.append('nut')

        if self.pasta_value == maximum_value:

            first_list_of_best_types.append('pasta')

        else:

            if self.pasta_value == second_maximum_value:

                second_list_of_best_types.append('pasta')

        if self.poultry_value == maximum_value:

            first_list_of_best_types.append('poultry')

        else:

            if self.poultry_value == second_maximum_value:

                second_list_of_best_types.append('poultry')

        if self.seafood_value == maximum_value:

            first_list_of_best_types.append('seafood')

        else:

            if self.seafood_value == second_maximum_value:

                second_list_of_best_types.append('seafood')

        if self.vegetable_value == maximum_value:

            first_list_of_best_types.append('vegetable')

        else:

            if self.vegetable_value == second_maximum_value:

                second_list_of_best_types.append('vegetable')

        dictionary_of_best_types['first'] = first_list_of_best_types
        dictionary_of_best_types['second'] = second_list_of_best_types

        return dictionary_of_best_types
