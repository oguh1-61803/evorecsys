# This class represents the restriction related to the healthiness of the food items.
class HealthyFoodRestriction:

    INTERPOLATION_REFERENCE_VALUE = 1.0

    # Constructor
    def __init__(self, protein, carbohydrate, sugar, fibre, fat, sat_fat, sodium):

        self.protein_reference_value = protein
        self.carbohydrate_reference_value = carbohydrate
        self.sugar_reference_value = sugar
        self.fibre_reference_value = fibre
        self.fat_limit_reference_value = fat
        self.saturated_fat_reference_value = sat_fat
        self.sodium_reference_value = sodium

    # This method evaluates the phenotype of individuals in terms of healthiness of food items contained in a meal.
    def evaluate(self, phenotype):

        protein_scores = []
        carbohydrate_scores = []
        sugar_scores = []
        fibre_scores = []
        fat_scores = []
        saturated_fat_scores = []
        sodium_scores = []

        for bundle in phenotype:

            meal = bundle.meal
            protein_score = self.__evaluate_exact_size_of_nutrient(self.protein_reference_value, meal.proteins)
            protein_scores.append(protein_score)
            carbohydrate_score = self.__evaluate_at_least_nutrient_size(self.carbohydrate_reference_value,
                                                                        meal.carbohydrates)
            carbohydrate_scores.append(carbohydrate_score)
            sugar_score = self.__evaluate_less_than_nutrient_size(self.sugar_reference_value, meal.sugars)
            sugar_scores.append(sugar_score)
            fibre_score = self.__evaluate_exact_size_of_nutrient(self.fibre_reference_value, meal.fiber)
            fibre_scores.append(fibre_score)
            fat_score = self.__evaluate_less_than_nutrient_size(self.fat_limit_reference_value, meal.fats)
            fat_scores.append(fat_score)
            saturated_fat_score = self.__evaluate_less_than_nutrient_size(self.saturated_fat_reference_value,
                                                                          meal.saturated_fats)
            saturated_fat_scores.append(saturated_fat_score)
            sodium_score = self.__evaluate_less_than_nutrient_size(self.sodium_reference_value, meal.sodium)
            sodium_scores.append(sodium_score)

        aptitude = self.__ponderate_aptitude(protein_scores, carbohydrate_scores, sugar_scores, fibre_scores,
                                             fat_scores, saturated_fat_scores, sodium_scores)

        return aptitude

    # This method calculates the final aptitude score of the individual.
    def __ponderate_aptitude(self, protein_scores, carbohydrate_scores, sugar_scores, fibre_scores, fat_scores,
                             saturated_fat_scores, sodium_scores):

        number_of_nutrients = 7
        number_of_bundles = len(protein_scores)
        protein_aptitude = 0.0
        carbohydrate_aptitude = 0.0
        sugar_aptitude = 0.0
        fibre_aptitude = 0.0
        fat_aptitude = 0.0
        saturated_fat_aptitude = 0.0
        sodium_aptitude = 0.0

        for index in range(0, number_of_bundles):

            protein_aptitude += protein_scores[index]
            carbohydrate_aptitude += carbohydrate_scores[index]
            sugar_aptitude += sugar_scores[index]
            fibre_aptitude += fibre_scores[index]
            fat_aptitude += fat_scores[index]
            saturated_fat_aptitude += saturated_fat_scores[index]
            sodium_aptitude += sodium_scores[index]

        summatory_of_aptitudes = (protein_aptitude / number_of_bundles) + (carbohydrate_aptitude / number_of_bundles) + \
                                 (sugar_aptitude / number_of_bundles) + (fibre_aptitude / number_of_bundles) + \
                                 (fat_aptitude / number_of_bundles) + (saturated_fat_aptitude / number_of_bundles) + \
                                 (sodium_aptitude / number_of_bundles)
        final_aptitude = summatory_of_aptitudes / number_of_nutrients

        return final_aptitude

    # This method evaluates if a nutrient size is equals to the reference size.
    def __evaluate_exact_size_of_nutrient(self, nutrient_reference_value, meal_nutrient_size):

        nutrient_difference = abs(nutrient_reference_value - meal_nutrient_size)

        if nutrient_difference >= nutrient_reference_value:

            nutrient_difference = nutrient_reference_value

        score = (nutrient_difference * self.INTERPOLATION_REFERENCE_VALUE) / nutrient_reference_value

        return score

    # This method evaluates if a nutrient size is less than the reference size.
    def __evaluate_less_than_nutrient_size(self, nutrient_reference_value, meal_nutrient_size):

        if meal_nutrient_size >= nutrient_reference_value:

            return 1.0

        else:

            nutrient_difference = nutrient_reference_value - (nutrient_reference_value - meal_nutrient_size)
            score = (nutrient_difference * self.INTERPOLATION_REFERENCE_VALUE) / nutrient_reference_value

            return score

    # This method evaluates if a nutrient size is has at least the same size as the reference size.
    def __evaluate_at_least_nutrient_size(self, nutrient_reference_value, meal_nutrient_size):

        if meal_nutrient_size < nutrient_reference_value or meal_nutrient_size >= (nutrient_reference_value * 2):

            return 1.0

        else:

            nutrient_difference = abs(nutrient_reference_value - meal_nutrient_size)
            score = (nutrient_difference * self.INTERPOLATION_REFERENCE_VALUE) / nutrient_reference_value

            return score

