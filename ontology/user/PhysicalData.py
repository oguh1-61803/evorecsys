# All necessary libraries.
import math


# This class represents the physical data of the current user.
class PhysicalData:

    # Constructor
    def __init__(self, female, age, height, weight, activity_level, goal, bundles=3):

        self.is_female = female
        self.age = age
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
        self.goal = goal
        self.maximum_number_of_calories = None
        self.number_of_bundles = bundles

        self.__calculate_adequate_number_of_calories()

    # This method calculates the number of intake calories recommended for the current user.
    def __calculate_adequate_number_of_calories(self, default_equation=0):

        if default_equation == 0:

            pre_calories = self.__calculate_by_harrisben_equation()

        else:

            pre_calories = self.__calculate_by_mifflin_equation()

        calories = self.__multiply_by_activity_constant(pre_calories)
        self.maximum_number_of_calories = self.__calculate_final_calories_by_wellbeing_goal(calories)

    # This method calculates the number of intake calories recommended to  the current user, considering their
    # wellbeing goal.
    def __calculate_final_calories_by_wellbeing_goal(self, calories):

        number_of_meals = 3

        if self.goal == 0:

            # Losing weight
            calories_constant = 551.26
            number_of_calories = (calories - calories_constant) / number_of_meals

            return math.ceil(number_of_calories)

        if self.goal == 1:

            # Maintaining weight
            calories_factor = 0.10
            number_of_calories = (calories + (calories * calories_factor)) / number_of_meals

            return math.ceil(number_of_calories)

        if self.goal == 2:

            # Gaining weight
            calories_constant = 551.26
            number_of_calories = (calories + calories_constant) / number_of_meals

            return math.ceil(number_of_calories)

        if self.goal == 3:

            # Gaining muscle mass
            male_calories_percentage = 0.2
            female_calories_percentage = 0.15

            if self.is_female:

                number_of_calories = (calories + (calories * female_calories_percentage)) / number_of_meals

                return math.ceil(number_of_calories)

            else:

                number_of_calories = (calories + (calories * male_calories_percentage)) / number_of_meals

                return math.ceil(number_of_calories)

    # This method defines a constant used to calculate the number of intake calories recommended to the current user.
    def __multiply_by_activity_constant(self, pre_calories):

        if self.activity_level == 0:

            not_active_constant = 1.2

            return pre_calories * not_active_constant

        if self.activity_level == 1:

            more_less_active_constant = 1.4

            return pre_calories * more_less_active_constant

        if self.activity_level == 2:

            active_constant = 1.6

            return pre_calories * active_constant

        if self.activity_level == 3:

            very_active_constant = 1.8

            return pre_calories * very_active_constant

    # This method calculates the number of calories using the Harrisben equation.
    def __calculate_by_harrisben_equation(self):

        if self.is_female == 0:

            constant = 655.0955
            weight_constant = 9.5634
            height_constant = 1.8449
            age_constant = 4.6756

            calories = constant + (weight_constant * self.weight) + (height_constant * self.height) - (age_constant *
                                                                                                       self.age)
            return calories

        else:

            constant = 66.4730
            weight_constant = 13.7516
            height_constant = 5.0033
            age_constant = 6.7550

            calories = constant + (weight_constant * self.weight) + (height_constant * self.height) - (age_constant *
                                                                                                       self.age)
            return calories

    # This method calculates the number of calories using the Mifflin equation.
    def __calculate_by_mifflin_equation(self):

        weight_constant = 10
        height_constant = 6.25
        age_constant = 5

        if self.is_female:

            female_constant = 161

            calories = (weight_constant * self.weight) + (height_constant * self.height) - \
                       (age_constant * self.age) - female_constant

            return calories

        else:

            male_constant = 5

            calories = (weight_constant * self.weight) + (height_constant * self.height) - \
                       (age_constant * self.age) + male_constant

            return calories
