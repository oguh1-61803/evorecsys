# All necessary libraries and imports from other files.
from src.database.Connection import Connection
from src.ontology.item.PA import PA
from src.ontology.item.Food import Food
import mysql.connector


# This class creates a connection to a MySQL database to retrieve food items data, physical activities data and
# food restrictions.
class ItemsConnection(Connection):

    # These values help to build queries.
    PREFERENCE_LIMIT = 1
    MAIN_VALUE = LUNCH_VALUE = "'1'"
    SIDE_VALUE = "'0'"

    # Constructor
    def __init__(self):

        super().__init__()

    # This method retrieves food items data and build food item objects according to the preferences
    # of the current user.
    def retrieve_food_items(self, food_preferences):

        self.connector = mysql.connector.connect(user=self.USER, password=self.PASSWORD, host=self.HOST,
                                                 database=self.DATA_BASE)
        cursor = self.connector.cursor()

        selected_food_items = food_preferences.get_selected_values(self.PREFERENCE_LIMIT)
        food_items = {}
        main_items = []
        side_items = []

        cursor.execute('SELECT * FROM evo_rec_sys_v2.food_vegetable;')

        for food in cursor:

            f = Food(food[1], "vegetable", food[2], food[3], food[4], food[5], food[6], food[7], food[8], food[9],
                     food[10], food[11], food[12], food[13], food[14], food[15], food[17])
            side_items.append(f)

        if len(selected_food_items) <= 0:

            cursor.execute('SELECT * FROM evo_rec_sys_v2.food_pasta WHERE is_main =' + self.MAIN_VALUE +
                           ' AND time_lunch = ' + self.LUNCH_VALUE + ';')

            for food in cursor:

                f = Food(food[1], "pasta", food[2], food[3], food[4], food[5], food[6], food[7], food[8], food[9],
                         food[10], food[11], food[12], food[13], food[14], food[15], food[17])
                main_items.append(f)

            cursor.execute('SELECT * FROM evo_rec_sys_v2.food_nut WHERE is_main =' + self.SIDE_VALUE +
                           ' AND time_lunch = ' + self.LUNCH_VALUE + ';')

            for food in cursor:

                f = Food(food[1], "nut", food[2], food[3], food[4], food[5], food[6], food[7], food[8], food[9],
                         food[10], food[11], food[12], food[13], food[14], food[15], food[17])
                side_items.append(f)

        else:

            for selected_food_item in selected_food_items:

                if selected_food_item == "vegetable":

                    continue

                cursor.execute('SELECT * FROM evo_rec_sys_v2.food_' + selected_food_item + ' WHERE is_main =' +
                               self.MAIN_VALUE + ' AND time_lunch = ' + self.LUNCH_VALUE + ';')

                for food in cursor:

                    f = Food(food[1], selected_food_item, food[2], food[3], food[4], food[5], food[6], food[7], food[8],
                             food[9], food[10], food[11], food[12], food[13], food[14], food[15], food[17])
                    main_items.append(f)

                cursor.execute('SELECT * FROM evo_rec_sys_v2.food_' + selected_food_item + ' WHERE is_main =' +
                               self.SIDE_VALUE + ' AND time_lunch = ' + self.LUNCH_VALUE + ';')

                for food in cursor:
                    f = Food(food[1], selected_food_item, food[2], food[3], food[4], food[5], food[6], food[7], food[8],
                             food[9], food[10], food[11], food[12], food[13], food[14], food[15], food[17])
                    side_items.append(f)

        cursor.close()
        self.connector.close()
        food_items["main"] = main_items
        food_items["side"] = side_items

        return food_items

    # This method retrieves physical activities data and build physical activity objects according to the preferences
    # of the current user.
    def retrieve_pa_items(self, pa_preferences, gaining_muscle_mass=None):

        self.connector = mysql.connector.connect(user=self.USER, password=self.PASSWORD, host=self.HOST,
                                                 database=self.DATA_BASE)
        cursor = self.connector.cursor()

        selected_pa_items = pa_preferences.get_selected_exercising_activities(self.PREFERENCE_LIMIT)
        intensity = pa_preferences.calculate_average_intensity()
        exercise_items = []

        if len(selected_pa_items) <= 0:

            cursor.execute('SELECT * FROM evo_rec_sys_v2.exercise_walking;')

            for exercise_item in cursor:

                pa = PA(exercise_item[1], "walking", exercise_item[2], exercise_item[3], exercise_item[4],
                        exercise_item[5])
                exercise_items.append(pa)

        else:

            for activity in selected_pa_items:

                cursor.execute('SELECT * FROM evo_rec_sys_v2.exercise_' + activity + ' WHERE intensity =' +
                               str(intensity)+';')

                for pa_item in cursor:

                    pa = PA(pa_item[1], activity, pa_item[2], pa_item[3], pa_item[4], pa_item[5])
                    exercise_items.append(pa)

            if gaining_muscle_mass is True:

                cursor.execute('SELECT * FROM evo_rec_sys_v2.exercise_conditioning WHERE id IN (3,4,5,7,8,11);')

                for pa_item in cursor:

                    pa = PA(pa_item[1], "conditioning", pa_item[2], pa_item[3], pa_item[4], pa_item[5])
                    exercise_items.append(pa)

        cursor.close()
        self.connector.close()

        return exercise_items

    # This method retrieves food restrictions according the genre and the age of the current user.
    def retrieve_healthy_food_restrictions(self, user_genre, user_age):

        self.connector = mysql.connector.connect(user=self.USER, password=self.PASSWORD, host=self.HOST,
                                                 database=self.DATA_BASE)
        cursor = self.connector.cursor()

        genre = str(int(user_genre))
        age = str(user_age)

        cursor.execute('SELECT * FROM evo_rec_sys_v2.restrictions_food WHERE genre ='+"'"+genre+"'"+' AND '+"'"+age+"'"
                       +' BETWEEN inferior_limit AND superior_limit;')

        healthy_restrictions = None

        for restriction in cursor:

            healthy_restrictions = (restriction[4], restriction[5], restriction[6], restriction[7], restriction[8],
                                    restriction[9], restriction[10])
        cursor.close()
        self.connector.close()

        return healthy_restrictions

    # This method retrieves all food items data and build food item objects.
    def retrieve_all_food_items(self):

        food_items_names = ["bread", "cereal", "dairy", "egg", "fish", "fruit", "grain", "legume", "meat", "nut",
                            "pasta", "poultry", "seafood", "vegetable"]
        food_items = {}
        main_items = []
        side_items = []

        self.connector = mysql.connector.connect(user=self.USER, password=self.PASSWORD, host=self.HOST,
                                                 database=self.DATA_BASE)
        cursor = self.connector.cursor()

        for food_item in food_items_names:

            cursor.execute('SELECT * FROM evo_rec_sys_v2.food_' + food_item + ' WHERE is_main =' +
                           self.MAIN_VALUE + ' AND time_lunch = ' + self.LUNCH_VALUE + ';')

            for food in cursor:

                f = Food(food[1], food_item, food[2], food[3], food[4], food[5], food[6], food[7], food[8],
                         food[9], food[10], food[11], food[12], food[13], food[14], food[15], food[17])
                main_items.append(f)

            cursor.execute('SELECT * FROM evo_rec_sys_v2.food_' + food_item + ' WHERE is_main =' +
                           self.SIDE_VALUE + ' AND time_lunch = ' + self.LUNCH_VALUE + ';')

            for food in cursor:
                f = Food(food[1], food_item, food[2], food[3], food[4], food[5], food[6], food[7], food[8],
                         food[9], food[10], food[11], food[12], food[13], food[14], food[15], food[17])
                side_items.append(f)

        cursor.close()
        self.connector.close()
        food_items["main"] = main_items
        food_items["side"] = side_items

        return food_items

    # This method retrieves all physical activities data and build physical activity objects.
    def retrieve_all_pa_items(self):

        pa_items_names = ["balance", "bicycling", "conditioning", "dancing", "running", "sports", "walking", "water"]
        pa_items = []

        self.connector = mysql.connector.connect(user=self.USER, password=self.PASSWORD, host=self.HOST,
                                                 database=self.DATA_BASE)
        cursor = self.connector.cursor()

        for activity in pa_items_names:

            cursor.execute('SELECT * FROM evo_rec_sys_v2.exercise_' + activity + ';')

            for pa_item in cursor:

                pa = PA(pa_item[1], activity, pa_item[2], pa_item[3], pa_item[4], pa_item[5])
                pa_items.append(pa)

        return pa_items
