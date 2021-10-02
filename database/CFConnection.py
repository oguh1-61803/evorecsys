# All necessary libraries and imports from other files.
from src.database.Connection import Connection
import mysql.connector


# This class creates a connection to a MySQL database to retrieve data of users. This data is used in the
# Collaborative filtering stage.
class CFConnection(Connection):

    # Constructor
    def __init__(self):

        super().__init__()

    # This method retrieves from the database all rows which contain the data of users.
    def retrieve_users_data(self):

        self.connector = mysql.connector.connect(user=self.USER, password=self.PASSWORD, host=self.HOST,
                                                 database=self.DATA_BASE)
        users_data = []
        cursor = self.connector.cursor()
        cursor.execute("SELECT gender,age,height,weight,activity_level,bread_pref,cereal_pref,dairy_pref,egg_pref,"
                       "fish_pref,fruits_pref,grains_pref,legumes_pref,meat_pref,nuts_pref,pasta_pref,poultry_pref,"
                       "seafood_pref,vegetables_pref,days_pref,minutes_pref,balance_pref,bicycling_pref,"
                       "conditioning_pref,dancing_pref,running_pref,sports_pref,walking_pref,water_pref,wellbeing "
                       "FROM evo_rec_sys_v2.cf_users_normalised_data;")

        for user_data in cursor:

            users_data.append(list(user_data))

        cursor.close()
        self.connector.close()

        return users_data

    # This method retrieves the most similar user data using its id.
    def retrieve_most_similar_user(self, user_id):

        self.connector = mysql.connector.connect(user=self.USER, password=self.PASSWORD, host=self.HOST,
                                                 database=self.DATA_BASE)
        cursor = self.connector.cursor()
        cursor.execute("SELECT gender,age,height,weight, activity_level,bread_pref,cereal_pref,dairy_pref,egg_pref,"
                       "fish_pref,fruits_pref,grains_pref,legumes_pref,meat_pref,nuts_pref,pasta_pref,poultry_pref,"
                       "seafood_pref,vegetables_pref,days_pref,minutes_pref,balance_pref,bicycling_pref,"
                       "conditioning_pref,dancing_pref,running_pref,sports_pref,walking_pref,water_pref,wellbeing "
                       "FROM evo_rec_sys_v2.cf_users_raw_data WHERE user_id=" + "'" + str(user_id) + "';")
        user_data = cursor.fetchall()

        if len(user_data) == 0:

            return -1

        else:

            return list(user_data[0])
