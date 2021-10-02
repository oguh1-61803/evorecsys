# This class represents the restriction related to the healthiness of the food items.
class UserPreferencesRestriction:

    INTERPOLATION_REFERENCE_VALUE = 1.0
    GAINING_MUSCLE_PHYSICAL_ACTIVITY_LIST = ["Calisthenics (sit ups, crunches)", "Calisthenics (push ups, pull ups)",
                                             "Resistance training (weight lifting)", "Circuit training",
                                             "Resistance training (weight)", "Video exercise workouts"]

    # Constructor
    def __init__(self, high_evaluated_food_types, high_evaluated_activity_types, muscle_mass=None):

        self.high_evaluated_food_types = high_evaluated_food_types
        self.high_evaluated_activity_types = high_evaluated_activity_types
        self.muscle_mass = muscle_mass

    # This method evaluates the phenotype of individuals in terms of the user preferences of food and physical activity.
    def evaluate(self, phenotype):

        if self.muscle_mass is None:

            food_attractiveness_scores = []
            pa_attractiveness_scores = []

            for bundle in phenotype:

                meal = bundle.meal
                food_attractiveness_score = self.__evaluate_food_attractiveness(meal)
                food_attractiveness_scores.append(food_attractiveness_score)
                pa = bundle.pa
                pa_attractiveness_score = self.__evaluate_exercising_attractiveness(pa.category)
                pa_attractiveness_scores.append(pa_attractiveness_score)

            aptitude = self.__ponderate_common_aptitude(food_attractiveness_scores, pa_attractiveness_scores)

            return aptitude

        else:

            food_attractiveness_scores = []
            pa_attractiveness_scores = []
            gaining_muscle_mass_scores = []

            for bundle in phenotype:

                meal = bundle.meal
                food_attractiveness_score = self.__evaluate_food_attractiveness(meal)
                food_attractiveness_scores.append(food_attractiveness_score)
                pa = bundle.pa
                exercising_attractiveness_score = self.__evaluate_exercising_attractiveness(pa.category)
                pa_attractiveness_scores.append(exercising_attractiveness_score)
                gaining_muscle_mass_score = self.__evaluate_gaining_muscle_mass_activity(pa.name)
                gaining_muscle_mass_scores.append(gaining_muscle_mass_score)

            aptitude = self.__ponderate_muscle_aptitude(food_attractiveness_scores, pa_attractiveness_scores,
                                                        gaining_muscle_mass_scores)
            return aptitude

    # This method calculates the final aptitude score of the individual.
    def __ponderate_common_aptitude(self, food_attractiveness_scores, exercising_attractiveness_scores):

        number_of_preferences = 2
        number_of_bundles = len(food_attractiveness_scores)
        food_attractiveness_aptitude = 0.0
        exercising_attractiveness_aptitude = 0.0

        for index in range(0, number_of_bundles):

            food_attractiveness_aptitude += food_attractiveness_scores[index]
            exercising_attractiveness_aptitude += exercising_attractiveness_scores[index]

        summatory_of_aptitudes = (food_attractiveness_aptitude / number_of_bundles) + \
                                 (exercising_attractiveness_aptitude / number_of_bundles)
        final_aptitude = summatory_of_aptitudes / number_of_preferences

        return final_aptitude

    # This method only applies if the user wants to gain muscle mass. It calculates the final aptitude score of
    # the individual.
    def __ponderate_muscle_aptitude(self, food_attractiveness_scores, exercising_attractiveness_scores,
                                    gaining_muscle_mass_scores):

        number_of_preferences = 3
        number_of_bundles = len(food_attractiveness_scores)
        food_attractiveness_aptitude = 0.0
        exercising_attractiveness_aptitude = 0.0
        gaining_muscle_mass_aptitude = 0.0

        for index in range(0, number_of_bundles):

            food_attractiveness_aptitude += food_attractiveness_scores[index]
            exercising_attractiveness_aptitude += exercising_attractiveness_scores[index]
            gaining_muscle_mass_aptitude += gaining_muscle_mass_scores[index]

        summatory_of_aptitudes = (food_attractiveness_aptitude / number_of_bundles) + \
                                 (exercising_attractiveness_aptitude / number_of_bundles) + \
                                 (gaining_muscle_mass_aptitude / number_of_bundles)
        final_aptitude = summatory_of_aptitudes / number_of_preferences

        return final_aptitude

    # This method evaluates how attractive are the suggested food items to the user.
    def __evaluate_food_attractiveness(self, meal):

        food_type_list = []
        main = meal.main_food_item.category
        food_type_list.append(main)

        for side_item in meal.side_food_items_list:

            food_type_list.append(side_item.category)

        food_type_set = set(food_type_list)
        first_high_evaluated = set(self.high_evaluated_food_types.get('first'))
        first_food_intersection = food_type_set.intersection(first_high_evaluated)

        if len(food_type_set) == len(first_food_intersection):

            return 0.0

        else:

            attractiveness_difference = len(food_type_set) - len(first_food_intersection)
            score = (attractiveness_difference * self.INTERPOLATION_REFERENCE_VALUE) / len(food_type_set)

            return score

    # This method evaluates how attractive are the suggested physical activities to the user.
    def __evaluate_exercising_attractiveness(self, pa_type):

        pa_set = set(pa_type)
        high_evaluated = set(self.high_evaluated_activity_types.get('first'))
        first_activity_intersection = high_evaluated.intersection(pa_set)

        if len(first_activity_intersection) == 1:

            return 0.0

        else:

            second_high_evaluated = set(self.high_evaluated_activity_types.get('second'))
            second_activity_intersection = second_high_evaluated.intersection(pa_set)

            if len(second_activity_intersection) == 1:

                return 0.5

        return 1.0

    # This method only applies if the user wants to gain muscle mass. It evaluates how attractive are the suggested
    # physical activities to the user.
    def __evaluate_gaining_muscle_mass_activity(self, pa_activity_name):

        if pa_activity_name in self.GAINING_MUSCLE_PHYSICAL_ACTIVITY_LIST:

            return 0.0

        else:

            return 0.20
