# This class represents the restriction related to the duration and intensity of the suggested physical
# activities.
class PARestriction:

    INTERPOLATION_REFERENCE_VALUE = 1.0

    # Constructor
    def __init__(self, spent_minutes):

        self.spent_minutes = spent_minutes

    # This method evaluates the phenotype of individuals in terms of physical activity duration and intensity.
    def evaluate(self, phenotype):

        duration_scores = []

        for bundle in phenotype:

            pa = bundle.pa
            duration_score = self.__evaluate_spent_time(pa.duration)
            duration_scores.append(duration_score)

        aptitude = self.__ponderate_aptitude(duration_scores)

        return aptitude

    # This method calculates the final aptitude score of the individual.
    def __ponderate_aptitude(self, duration_scores):

        number_of_bundles = len(duration_scores)
        duration_aptitude = 0.0

        for index in range(0, number_of_bundles):

            duration_aptitude += duration_scores[index]

        summatory_of_aptitudes = duration_aptitude / number_of_bundles

        return summatory_of_aptitudes

    # This method evaluates the physical activity in terms of the duration of the suggested physical activity.
    def __evaluate_spent_time(self, duration):

        time_difference = abs(self.spent_minutes - duration)

        if time_difference >= self.spent_minutes:

            time_difference = self.spent_minutes

        score = (time_difference * self.INTERPOLATION_REFERENCE_VALUE) / self.spent_minutes

        return score
