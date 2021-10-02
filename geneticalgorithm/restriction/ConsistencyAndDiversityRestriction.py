# This class represents the restriction related to the consistency and diversity of the recommendations.
class ConsistencyAndDiversityRestriction:

    INTERPOLATION_REFERENCE_VALUE = 1.0

    # Constructor
    def __init__(self):

        pass

    # This method evaluates the phenotype of individuals in terms of consistency and diversity.
    def evaluate(self, phenotype):

        main_food_item_name_list = []
        side_food_item_name_list = []
        main_food_item_type_list = []
        side_food_item_type_list = []
        pa_item_name_list = []
        size_scores = []

        for bundle in phenotype:

            meal = bundle.meal
            size_score = self.__evaluate_size_consistency(meal)
            size_scores.append(size_score)
            main_food_item_name_list.append(meal.main_food_item.name)
            main_food_item_type_list.append(meal.main_food_item.category)
            pa_item_name_list.append(bundle.pa.name)

            for food_item in meal.side_food_items_list:

                side_food_item_name_list.append(food_item.name)
                side_food_item_type_list.append(food_item.category)

        main_food_diversity_name_score = self.__evaluate_food_diversity(main_food_item_name_list)
        side_food_diversity_name_score = self.__evaluate_food_diversity(side_food_item_name_list)
        main_food_diversity_type_score = self.__evaluate_food_diversity(main_food_item_type_list)
        side_food_diversity_type_score = self.__evaluate_food_diversity(side_food_item_type_list)
        exercise_diversity_score = self.__evaluate_exercising_diversity(pa_item_name_list)
        aptitude = self.__ponderate_aptitude(main_food_diversity_name_score, side_food_diversity_name_score,
                                             main_food_diversity_type_score, side_food_diversity_type_score,
                                             size_scores, exercise_diversity_score)

        return aptitude

    # This method calculates the final aptitude score of the individual.
    def __ponderate_aptitude(self, main_food_diversity_name_score, side_food_diversity_name_score,
                             main_food_diversity_type_score, side_food_diversity_type_score, size_scores,
                             exercise_diversity_score):

        number_of_elements = 6
        number_of_bundles = len(size_scores)
        size_aptitude = 0.0

        for index in range(0, number_of_bundles):

            size_aptitude += size_scores[index]

        summatory_of_aptitudes = main_food_diversity_name_score + side_food_diversity_name_score + \
                                 main_food_diversity_type_score + side_food_diversity_type_score +\
                                 (size_aptitude / number_of_bundles) + exercise_diversity_score
        aptitude = summatory_of_aptitudes / number_of_elements

        return aptitude

    # This method evaluates the food diversity of the meal in each bundle of the individual.
    def __evaluate_food_diversity(self, food_name_list):

        food_names_set = set(food_name_list)

        if len(food_name_list) == len(food_names_set):

            return 0.0

        else:

            diversity_difference = len(food_name_list) - len(food_names_set)
            score = (diversity_difference * self.INTERPOLATION_REFERENCE_VALUE) / len(food_name_list)

            return score

    # This method evaluates the physical activity diversity in each bundle of the individual.
    def __evaluate_exercising_diversity(self, exercise_name_list):

        exercise_name_set = set(exercise_name_list)

        if len(exercise_name_list) == len(exercise_name_set):

            return 0.0

        else:

            diversity_difference = len(exercise_name_list) - len(exercise_name_set)
            score = (diversity_difference * self.INTERPOLATION_REFERENCE_VALUE) / len(exercise_name_list)

            return score

    # This method evaluates the food size consistency in the meal in each bundle of the individual.
    def __evaluate_size_consistency(self, meal):

        side_calories = meal.serving_size - meal.main_food_item.serving_size
        side_calories_reference = side_calories / len(meal.side_food_items_list)
        side_scores = []

        for side_item in meal.side_food_items_list:

            calories_difference = abs(side_calories_reference - side_item.serving_size)

            if calories_difference > side_calories_reference:

                side_scores.append(1.0)

            else:

                score = (calories_difference * self.INTERPOLATION_REFERENCE_VALUE) / side_calories_reference
                side_scores.append(score)

        aux_score = 0.0

        for score in side_scores:

            aux_score += score

        final_score = aux_score / len(side_scores)

        return final_score
