# All necessary libraries and imports from other files.
from sklearn.metrics.pairwise import cosine_similarity
from src.database.CFConnection import CFConnection
from operator import itemgetter
import numpy


# This class retrieves the most similar user data to the data of the current user by nearest-neighbour
# Collaborative Filtering strategy. It creates a connection to a relational database.
class CollaborativeFiltering:

    # Static indexes of the vector that represents the data of the users.
    PHYSICAL_DATA_INDEX = 5
    FOOD_DATA_INDEX = 12
    EXERCISING_DATA_INDEX = 20
    K_NEIGHBOURS = 10

    # Constructor
    def __init__(self):

        self.age_index_list = [1]
        self.age_values = [10, 95]
        self.height_index_list = [2]
        self.height_values = [110, 220]
        self.weight_index_list = [3]
        self.weight_values = [30.0, 130.0]
        self.activity_index_list = [4]
        self.activity_values = [0, 3]
        self.common_range_index_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26,
                                        27, 28]
        self.common_values = [0, 5]
        self.days_index_list = [19]
        self.days_values = [0, 7]
        self.minutes_index_list = [20]
        self.minutes_values = [0, 120]
        self.goal_index_list = [29]
        self.goal_values = [0, 3]

        self.connection = CFConnection()

    # This method creates a normalised vector using the data of the current user which be used to perform the
    # comparison against all data stored in the database. It returns the most similar user data. If there is no
    # result, the method returns -1.
    def get_similar_user_data_with_single_vector(self, user_data):

        user_data_vector = self.normalise_user_data(user_data)
        users_data_matrix = self.connection.retrieve_users_data()
        user_vector = numpy.array(user_data_vector).reshape(1, -1)
        users_matrix = numpy.array(users_data_matrix)
        similarity = cosine_similarity(user_vector, users_matrix)
        similarity_list = []

        for index in range(0, len(similarity[0])):

            similarity_tuple = (index, similarity[0][index])
            similarity_list.append(similarity_tuple)

        sorted_similarity = sorted(similarity_list, key=itemgetter(1), reverse=True)
        similar_user_data = self.connection.retrieve_most_similar_user(sorted_similarity[0][0])

        if similar_user_data == -1:

            return -1

        else:

            return similar_user_data

    # This method normalises a vector of user data.
    def normalise_user_data(self, user_data):

        normalised_user_data = []

        for index in range(0, len(user_data)):

            if index in self.age_index_list:
                normalised_value = self.__normalise_value(user_data[index], self.age_values[0], self.age_values[1])
                normalised_user_data.append(normalised_value)

                continue

            if index in self.height_index_list:
                normalised_value = self.__normalise_value(user_data[index], self.height_values[0],
                                                          self.height_values[1])
                normalised_user_data.append(normalised_value)

                continue

            if index in self.weight_index_list:
                normalised_value = self.__normalise_value(user_data[index], self.weight_values[0],
                                                          self.weight_values[1])
                normalised_user_data.append(normalised_value)

                continue

            if index in self.activity_index_list:
                normalised_value = self.__normalise_value(user_data[index], self.activity_values[0],
                                                          self.activity_values[1])
                normalised_user_data.append(normalised_value)

                continue

            if index in self.common_range_index_list:
                normalised_value = self.__normalise_value(user_data[index], self.common_values[0],
                                                          self.common_values[1])
                normalised_user_data.append(normalised_value)

                continue

            if index in self.days_index_list:
                normalised_value = self.__normalise_value(user_data[index], self.days_values[0], self.days_values[1])
                normalised_user_data.append(normalised_value)

                continue

            if index in self.minutes_index_list:
                normalised_value = self.__normalise_value(user_data[index], self.minutes_values[0],
                                                          self.minutes_values[1])
                normalised_user_data.append(normalised_value)

                continue

            if index in self.goal_index_list:
                normalised_value = self.__normalise_value(user_data[index], self.goal_values[0], self.goal_values[1])
                normalised_user_data.append(normalised_value)

                continue

            normalised_user_data.append(user_data[index])

        return normalised_user_data

    def __normalise_value(self, value, minimum_value, maximum_value):

        normalised_value = round((value - minimum_value) / (maximum_value - minimum_value), 5)

        return normalised_value
