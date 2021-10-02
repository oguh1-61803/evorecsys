# All necessary libraries and imports from other files.
from src.database.Connection import Connection
import mysql.connector
import string
import random


# This class creates a connection to a MySQL database to insert the feedback of users. It considers both, bundle
# and four Recommender Systems metrics feedback.
class FeedbackConnection(Connection):

    # Constructor
    def __init__(self):

        super().__init__()

    # This method only inserts the feedback related to the recommended bundles.
    def store_bundles_feedback(self, no_response_counter, rec1_meal, rec1_exercise, rec1_favorite, rec2_meal,
                               rec2_exercise, rec2_favorite, rec3_meal, rec3_exercise, rec3_favorite):

        self.connector = mysql.connector.connect(user=self.USER, password=self.PASSWORD, host=self.HOST,
                                                 database=self.DATA_BASE)
        unique_id = self.__generate_id()
        cursor = self.connector.cursor()
        sql_sentence = ("INSERT INTO evo_rec_sys_v2.user_feedback (id,no_response_counter,meal_0,pa_0,is_favorite_0,"
                        "meal_1,pa_1,is_favorite_1,meal_2,pa_2,is_favorite_2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                        "%s);")
        sql_values = (unique_id, no_response_counter, rec1_meal, rec1_exercise, rec1_favorite, rec2_meal, rec2_exercise,
                      rec2_favorite, rec3_meal, rec3_exercise, rec3_favorite)
        cursor.execute(sql_sentence, sql_values)
        self.connector.commit()
        cursor.close()
        self.connector.close()

    # This method inserts the full feedback: bundles and Recommender Systems metrics.
    def store_full_feedback(self, no_response_counter, rec1_meal, rec1_exercise, rec1_favorite, rec2_meal,
                            rec2_exercise, rec2_favorite, rec3_meal, rec3_exercise, rec3_favorite, diversity,
                            surprising, reliability, healthy):
        unique_id = self.__generate_id()
        cursor = self.connector.cursor()
        sql_sentence = ("INSERT INTO evo_rec_sys_v2.user_feedback (id,no_response_counter,meal_0,pa_0,is_favorite_0,"
                        "meal_1,pa_1,is_favorite_1,meal_2,pa_2,is_favorite_2,diversity,surprising,reliability,healthy) "
                        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
        sql_values = (unique_id, no_response_counter, rec1_meal, rec1_exercise, rec1_favorite, rec2_meal, rec2_exercise,
                      rec2_favorite, rec3_meal, rec3_exercise, rec3_favorite, diversity, surprising, reliability,
                      healthy)
        cursor.execute(sql_sentence, sql_values)
        self.connector.commit()
        cursor.close()
        self.connector.close()

    # This method generates a random id.
    def __generate_id(self, length=17):

        self.connector = mysql.connector.connect(user=self.USER, password=self.PASSWORD, host=self.HOST,
                                                 database=self.DATA_BASE)
        founded_id = False
        unique_id = None

        while founded_id is False:

            letters_and_digits = string.ascii_letters + string.digits
            unique_id = ''.join(random.choice(letters_and_digits) for _ in range(length))
            cursor = self.connector.cursor()
            sql_sentence = ("SELECT * FROM evo_rec_sys_v2.user_feedback WHERE id=" + "'" + unique_id + "';")
            cursor.execute(sql_sentence)
            id_data = cursor.fetchall()

            if len(id_data) == 0:

                founded_id = True

        return unique_id
