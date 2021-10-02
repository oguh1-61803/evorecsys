# This class represents the physical activity preferences of the current user.
class PAPreferenceData:

    # These values are used as static reference values.
    LOW_DAY_VALUE = 2
    MODERATE_DAY_VALUE = 5
    INTENSE_DAY_VALUE = 7
    LOW_MINUTE_VALUE = 45
    MODERATE_MINUTE_VALUE = 90
    INTENSE_MINUTE_VALUE = 120

    # Constructor
    def __init__(self, days, minutes, balance, bicycling, conditioning, dancing, running, sports, walking, water):

        self.days = days
        self.minutes = minutes
        self.balance_value = balance
        self.bicycling_value = bicycling
        self.conditioning_value = conditioning
        self.dancing_value = dancing
        self.running_value = running
        self.sports_value = sports
        self.walking_value = walking
        self.water_value = water

    # This method gets the values associated to the preference of each physical activity category.
    def get_selected_exercising_activities(self, limit):

        exercising_list = []

        if self.balance_value >= limit:

            exercising_list.append('balance')

        if self.bicycling_value >= limit:

            exercising_list.append('bicycling')

        if self.conditioning_value >= limit:

            exercising_list.append('conditioning')

        if self.dancing_value >= limit:

            exercising_list.append('dancing')

        if self.running_value >= limit:

            exercising_list.append('running')

        if self.sports_value >= limit:

            exercising_list.append('sports')

        if self.walking_value >= limit:

            exercising_list.append('walking')

        if self.water_value >= limit:

            exercising_list.append('water')

        return exercising_list

    # This method gets the highest evaluated types of physical activities by the user.
    def get_higher_evaluated_activities(self):

        dictionary_of_best_types = {}
        first_list_of_best_types = []
        second_list_of_best_types = []
        list_of_activity_values = [self.balance_value, self.bicycling_value, self.conditioning_value,
                                   self.dancing_value, self.running_value, self.sports_value, self.walking_value,
                                   self.water_value]
        maximum_activity_value = max(list_of_activity_values)
        second_maximum_activity_value = maximum_activity_value - 1

        if self.balance_value == maximum_activity_value:

            first_list_of_best_types.append('balance')

        elif self.balance_value == second_maximum_activity_value:

            second_list_of_best_types.append('balance')

        if self.bicycling_value == maximum_activity_value:

            first_list_of_best_types.append('bicycling')

        elif self.bicycling_value == second_maximum_activity_value:

            second_list_of_best_types.append('bicycling')

        if self.conditioning_value == maximum_activity_value:

            first_list_of_best_types.append('conditioning')

        elif self.conditioning_value == second_maximum_activity_value:

            second_list_of_best_types.append('conditioning')

        if self.dancing_value == maximum_activity_value:

            first_list_of_best_types.append('dancing')

        elif self.dancing_value == second_maximum_activity_value:

            second_list_of_best_types.append('dancing')

        if self.running_value == maximum_activity_value:

            first_list_of_best_types.append('running')

        elif self.running_value == second_maximum_activity_value:

            second_list_of_best_types.append('running')

        if self.sports_value == maximum_activity_value:

            first_list_of_best_types.append('sports')

        elif self.sports_value == second_maximum_activity_value:

            second_list_of_best_types.append('sports')

        if self.walking_value == maximum_activity_value:

            first_list_of_best_types.append('walking')

        elif self.walking_value == second_maximum_activity_value:

            second_list_of_best_types.append('walking')

        if self.water_value == maximum_activity_value:

            first_list_of_best_types.append('water')

        elif self.water_value == second_maximum_activity_value:

            second_list_of_best_types.append('water')

        dictionary_of_best_types["first"] = first_list_of_best_types
        dictionary_of_best_types["second"] = second_list_of_best_types

        return dictionary_of_best_types

    # This method calculates the intensity of the recommended physical activities using data of the current user.
    # Namely, average minutes and average days that the user usually spends for exercising.
    def calculate_average_intensity(self):

        if self.minutes <= self.LOW_MINUTE_VALUE:

            if self.days <= self.LOW_DAY_VALUE:

                activity_intensity = 1

                return activity_intensity

            if self.LOW_DAY_VALUE < self.days <= self.MODERATE_DAY_VALUE:

                activity_intensity = 1

                return activity_intensity

            if self.MODERATE_DAY_VALUE < self.days <= self.INTENSE_DAY_VALUE:

                activity_intensity = 0

                return activity_intensity

        if self.LOW_MINUTE_VALUE < self.minutes <= self.MODERATE_MINUTE_VALUE:

            if self.days <= self.LOW_DAY_VALUE:

                activity_intensity = 2

                return activity_intensity

            if self.LOW_DAY_VALUE < self.days <= self.MODERATE_DAY_VALUE:

                activity_intensity = 1

                return activity_intensity

            if self.MODERATE_DAY_VALUE < self.days <= self.INTENSE_DAY_VALUE:

                activity_intensity = 0

                return activity_intensity

        if self.MODERATE_MINUTE_VALUE < self.minutes <= self.INTENSE_MINUTE_VALUE:

            if self.days <= self.LOW_DAY_VALUE:

                activity_intensity = 2

                return activity_intensity

            if self.LOW_DAY_VALUE < self.days <= self.MODERATE_DAY_VALUE:

                activity_intensity = 2

                return activity_intensity

            if self.MODERATE_DAY_VALUE < self.days <= self.INTENSE_DAY_VALUE:

                activity_intensity = 1

                return activity_intensity

