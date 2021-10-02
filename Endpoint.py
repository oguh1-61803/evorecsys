# This implemented model of EvoRecSys has been designed as a web-based system. This file, which is a minimal endpoint,
# controls the full workflow of the system.


# All necessary libraries and imports from other files.
from src.collaborativefiltering.CollaborativeFiltering import CollaborativeFiltering
from src.geneticalgorithm.GeneticAlgorithm import GeneticAlgorithm
from src.database.FeedbackConnection import FeedbackConnection
import tornado.httpserver
import tornado.escape
import tornado.ioloop
import tornado.web
import os


# This class loads the cover of EvoRecSys.
class IndexEvoRecSys(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/index.html")
        self.clear_all_cookies()

        return

    def post(self):

        self.set_cookie("test-cookie", "test", expires_days=1, httponly=True)
        self.redirect("/start")

        return


# This class loads the second page of the workflow.
class Start(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        if self.get_cookie("test-cookie") is None:

            self.redirect("/no-cookies")

            return

        self.render("templates/pages/start.html")

        return

    def post(self):

        continuation = str(self.get_body_argument("continuation", ""))

        if continuation == 'No':

            self.clear_all_cookies()
            self.redirect("/")
            self.on_connection_close()

            return

        self.redirect('/physical-I')

        return


# This class loads the first step of physical data acquisition of the user; we obtain their age and genre.
class PhysicalDataI(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/physical-I.html")

        return

    def post(self):

        age = str(self.get_body_argument("age", ""))
        gen = str(self.get_body_argument("genre", ""))

        if gen == "on":

            gender = 1.0

        else:

            gender = 0.0

        self.set_cookie("age", age, expires_days=1, httponly=True)
        self.set_cookie("gender", str(gender), expires_days=1, httponly=True)
        self.redirect("/physical-II")

        return


# This class loads the second step of physical data acquisition of the user; we obtain their height and weight.
class PhysicalDataII(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/physical-II.html")

        return

    def post(self):

        h = float(self.get_body_argument("height", ""))
        height = h*100
        weight = str(self.get_body_argument("weight", ""))
        self.set_cookie("height", str(height), expires_days=1, httponly=True)
        self.set_cookie("weight", weight, expires_days=1, httponly=True)
        self.redirect("/physical-III")

        return


# This class loads the third step of physical data acquisition of the user; we obtain their activity level.
class PhysicalDataIII(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/physical-III.html")

        return

    def post(self):

        level = str(self.get_body_argument("active", ""))
        self.set_cookie("level", level, expires_days=1, httponly=True)
        self.redirect("/food-I")

        return


# This class loads the first step of food preferences acquisition of the user; we obtain bread
# and cereal preferences.
class FoodDataI(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/food-I.html")

        return

    def post(self):

        bread = str(self.get_body_argument("bread", ""))
        cereal = str(self.get_body_argument("cereal", ""))
        self.set_cookie("bread", bread, expires_days=1, httponly=True)
        self.set_cookie("cereal", cereal, expires_days=1, httponly=True)
        self.redirect("/food-II")

        return


# This class loads the second step of food preferences acquisition of the user; we obtain dairy, egg
# and fish preferences.
class FoodDataII(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/food-II.html")

        return

    def post(self):

        dairy = str(self.get_body_argument("dairy", ""))
        egg = str(self.get_body_argument("egg", ""))
        fish = str(self.get_body_argument("fish", ""))
        self.set_cookie("dairy", dairy, expires_days=1, httponly=True)
        self.set_cookie("egg", egg, expires_days=1, httponly=True)
        self.set_cookie("fish", fish, expires_days=1, httponly=True)
        self.redirect("/food-III")

        return


# This class loads the third step of food preferences acquisition of the user; we obtain fruit, grain
# and legume preferences.
class FoodDataIII(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/food-III.html")

        return

    def post(self):

        fruit = str(self.get_body_argument("fruit", ""))
        grain = str(self.get_body_argument("grain", ""))
        legume = str(self.get_body_argument("legume", ""))
        self.set_cookie("fruit", fruit, expires_days=1, httponly=True)
        self.set_cookie("grain", grain, expires_days=1, httponly=True)
        self.set_cookie("legume", legume, expires_days=1, httponly=True)
        self.redirect("/food-IV")

        return


# This class loads the fourth step of food preferences acquisition of the user; we obtain meat, nut
# and pasta preferences.
class FoodDataIV(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/food-IV.html")

        return

    def post(self):

        meat = str(self.get_body_argument("meat", ""))
        nut = str(self.get_body_argument("nut", ""))
        pasta = str(self.get_body_argument("pasta", ""))
        self.set_cookie("meat", meat, expires_days=1, httponly=True)
        self.set_cookie("nut", nut, expires_days=1, httponly=True)
        self.set_cookie("pasta", pasta, expires_days=1, httponly=True)
        self.redirect("/food-V")

        return


# This class loads the fifth step of food preferences acquisition of the user; we obtain poultry, seafood
# and vegetable preferences.
class FoodDataV(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/food-V.html")

        return

    def post(self):

        poultry = str(self.get_body_argument("poultry", ""))
        seafood = str(self.get_body_argument("seafood", ""))
        vegetable = str(self.get_body_argument("vegetable", ""))
        self.set_cookie("poultry", poultry, expires_days=1, httponly=True)
        self.set_cookie("seafood", seafood, expires_days=1, httponly=True)
        self.set_cookie("vegetable", vegetable, expires_days=1, httponly=True)
        self.redirect("/exercising-I")

        return


# This class loads the first step of exercising preferences acquisition of the user; we obtain how many days, and
# how many minutes the user usually spends on exercising.
class ExercisingDataI(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/exercising-I.html")

        return

    def post(self):

        days = str(self.get_body_argument("day", ""))
        minutes = str(self.get_body_argument("minute", ""))
        self.set_cookie("days", days, expires_days=1, httponly=True)
        self.set_cookie("minutes", minutes, expires_days=1, httponly=True)
        self.redirect("/exercising-II")

        return


# This class loads the second step of exercising preferences acquisition of the user; we obtain balance, bicycling
# and conditioning preferences.
class ExercisingDataII(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/exercising-II.html")

        return

    def post(self):

        balance = str(self.get_body_argument("balance", ""))
        bicycling = str(self.get_body_argument("bicycling", ""))
        conditioning = str(self.get_body_argument("conditioning", ""))
        self.set_cookie("balance", balance, expires_days=1, httponly=True)
        self.set_cookie("bicycling", bicycling, expires_days=1, httponly=True)
        self.set_cookie("conditioning", conditioning, expires_days=1, httponly=True)
        self.redirect("/exercising-III")

        return


# This class loads the third step of exercising preferences acquisition of the user; we obtain dancing, running
# and sports preferences.
class ExercisingDataIII(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/exercising-III.html")

        return

    def post(self):

        dancing = str(self.get_body_argument("dancing", ""))
        running = str(self.get_body_argument("running", ""))
        sport = str(self.get_body_argument("sport", ""))
        self.set_cookie("dancing", dancing, expires_days=1, httponly=True)
        self.set_cookie("running", running, expires_days=1, httponly=True)
        self.set_cookie("sport", sport, expires_days=1, httponly=True)
        self.redirect("/exercising-IV")

        return


# This class loads the fourth step of exercising preferences acquisition of the user; we obtain walking and water
# activities preferences.
class ExercisingDataIV(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/exercising-IV.html")

        return

    def post(self):

        walking = str(self.get_body_argument("walking", ""))
        water = str(self.get_body_argument("water", ""))
        self.set_cookie("walking", walking, expires_days=1, httponly=True)
        self.set_cookie("water", water, expires_days=1, httponly=True)
        self.redirect("/goal")

        return


# This class loads the stage where the wellbeing goal is chosen by the user.
class GoalData(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/goal.html")

        return

    def post(self):

        goal = str(self.get_body_argument("goal", ""))
        self.set_cookie("goal", goal, expires_days=1, httponly=True)
        self.redirect("/process-data")

        return


# This class loads the stage where the Genetic Algorithm uses as main input the data of the current user. Moreover, the
# Collaborative Filtering process takes place.
class ProcessData(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/process-data.html")

        return

    def post(self):

        user_data = [float(self.get_cookie("gender")),  #0
                     float(self.get_cookie("age")),
                     float(self.get_cookie("height")),
                     float(self.get_cookie("weight")),  #3
                     float(self.get_cookie("level")),
                     float(self.get_cookie("bread")),
                     float(self.get_cookie("cereal")),
                     float(self.get_cookie("dairy")),
                     float(self.get_cookie("egg")),     #8
                     float(self.get_cookie("fish")),
                     float(self.get_cookie("fruit")),
                     float(self.get_cookie("grain")),   #11
                     float(self.get_cookie("legume")),
                     float(self.get_cookie("meat")),
                     float(self.get_cookie("nut")),
                     float(self.get_cookie("pasta")),   #15
                     float(self.get_cookie("poultry")),
                     float(self.get_cookie("seafood")),
                     float(self.get_cookie("vegetable")), #18
                     float(self.get_cookie("days")),
                     float(self.get_cookie("minutes")),
                     float(self.get_cookie("balance")),   #21
                     float(self.get_cookie("bicycling")),
                     float(self.get_cookie("conditioning")),
                     float(self.get_cookie("dancing")),
                     float(self.get_cookie("running")),    #25
                     float(self.get_cookie("sport")),
                     float(self.get_cookie("walking")),
                     float(self.get_cookie("water")),
                     float(self.get_cookie("goal")),       #29
                     ]

        # This object retrieves the most similar user data to the data of the current user by nearest-neighbour
        # Collaborative Filtering strategy.
        cf = CollaborativeFiltering()
        similar_user_data = cf.get_similar_user_data_with_single_vector(user_data)

        if similar_user_data == -1:

            similar_user_data = user_data

        not_answered_counter = 0

        for index in range(0, len(user_data)):

            if user_data[index] == -1.0:

                user_data[index] = 2.0
                not_answered_counter += 1

            elif user_data[index] == 0.0 and index == 19:

                user_data[index] = 3
                not_answered_counter += 1

            elif user_data[index] == 0.0 and index == 20:

                user_data[index] = 30
                not_answered_counter += 1

        self.set_cookie("unanswered", str(not_answered_counter), expires_days=1, httponly=True)

        # This object creates an instance of a Genetic Algorithm and both user_data and most similar user data are the
        # main parameters of it.
        ga = GeneticAlgorithm(user_data, similar_user_data)
        suggested_bundles = ga.execute_genetic_algorithm()

        me0main_ = suggested_bundles[0].meal.main_food_item.name
        me0main = me0main_.replace(" ", "_")
        me0side0_ = suggested_bundles[0].meal.side_food_items_list[0].name
        me0side0 = me0side0_.replace(" ", "_")
        me0side1_ = suggested_bundles[0].meal.side_food_items_list[1].name
        me0side1 = me0side1_.replace(" ", "_")
        me0side2_ = suggested_bundles[0].meal.side_food_items_list[2].name
        me0side2 = me0side2_.replace(" ", "_")
        pa0name_ = suggested_bundles[0].pa.name
        pa0name = pa0name_.replace(" ", "_")
        me1main_ = suggested_bundles[1].meal.main_food_item.name
        me1main = me1main_.replace(" ", "_")
        me1side0_ = suggested_bundles[1].meal.side_food_items_list[0].name
        me1side0 = me1side0_.replace(" ", "_")
        me1side1_ = suggested_bundles[1].meal.side_food_items_list[1].name
        me1side1 = me1side1_.replace(" ", "_")
        me1side2_ = suggested_bundles[1].meal.side_food_items_list[2].name
        me1side2 = me1side2_.replace(" ", "_")
        pa1name_ = suggested_bundles[1].pa.name
        pa1name = pa1name_.replace(" ", "_")
        me2main_ = suggested_bundles[2].meal.main_food_item.name
        me2main = me2main_.replace(" ", "_")
        me2side0_ = suggested_bundles[2].meal.side_food_items_list[0].name
        me2side0 = me2side0_.replace(" ", "_")
        me2side1_ = suggested_bundles[2].meal.side_food_items_list[1].name
        me2side1 = me2side1_.replace(" ", "_")
        me2side2_ = suggested_bundles[2].meal.side_food_items_list[2].name
        me2side2 = me2side2_.replace(" ", "_")
        pa2name_ = suggested_bundles[2].pa.name
        pa2name = pa2name_.replace(" ", "_")

        self.set_cookie('me0-main', me0main, expires_days=1, httponly=True)
        self.set_cookie("me0-side0", me0side0, expires_days=1, httponly=True)
        self.set_cookie("me0-side1", me0side1, expires_days=1, httponly=True)
        self.set_cookie("me0-side2", me0side2, expires_days=1, httponly=True)
        self.set_cookie("pa0-name", pa0name, expires_days=1, httponly=True)
        self.set_cookie("pa0-duration", str(suggested_bundles[0].pa.duration), expires_days=1, httponly=True)
        self.set_cookie("me1-main", me1main, expires_days=1, httponly=True)
        self.set_cookie("me1-side0", me1side0, expires_days=1, httponly=True)
        self.set_cookie("me1-side1", me1side1, expires_days=1, httponly=True)
        self.set_cookie("me1-side2", me1side2, expires_days=1, httponly=True)
        self.set_cookie("pa1-name", pa1name, expires_days=1, httponly=True)
        self.set_cookie("pa1-duration", str(suggested_bundles[1].pa.duration), expires_days=1, httponly=True)
        self.set_cookie("me2-main", me2main, expires_days=1, httponly=True)
        self.set_cookie("me2-side0", me2side0, expires_days=1, httponly=True)
        self.set_cookie("me2-side1", me2side1, expires_days=1, httponly=True)
        self.set_cookie("me2-side2", me2side2, expires_days=1, httponly=True)
        self.set_cookie("pa2-name", pa2name, expires_days=1, httponly=True)
        self.set_cookie("pa2-duration", str(suggested_bundles[2].pa.duration), expires_days=1, httponly=True)
        self.redirect("/recommendations")

        return


# This class loads the stage where the recommendations built by the Genetic Algorithm are presented to the user. In
# addition, we get their feedback about the recommendations.
class Recommendations(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        me0main_ = str(self.get_cookie("me0-main"))
        me0main = me0main_.replace("_", " ")
        me0side0_ = str(self.get_cookie("me0-side0"))
        me0side0 = me0side0_.replace("_", " ")
        me0side1_ = str(self.get_cookie("me0-side1"))
        me0side1 = me0side1_.replace("_", " ")
        me0side2_ = str(self.get_cookie("me0-side2"))
        me0side2 = me0side2_.replace("_", " ")
        pa0name_ = str(self.get_cookie("pa0-name"))
        pa0name = pa0name_.replace("_", " ")
        me1main_ = str(self.get_cookie("me1-main"))
        me1main = me1main_.replace("_", " ")
        me1side0_ = str(self.get_cookie("me1-side0"))
        me1side0 = me1side0_.replace("_", " ")
        me1side1_ = str(self.get_cookie("me1-side1"))
        me1side1 = me1side1_.replace("_", " ")
        me1side2_ = str(self.get_cookie("me1-side2"))
        me1side2 = me1side2_.replace("_", " ")
        pa1name_ = str(self.get_cookie("pa1-name"))
        pa1name = pa1name_.replace("_", " ")
        me2main_ = str(self.get_cookie("me2-main"))
        me2main = me2main_.replace("_", " ")
        me2side0_ = str(self.get_cookie("me2-side0"))
        me2side0 = me2side0_.replace("_", " ")
        me2side1_ = str(self.get_cookie("me2-side1"))
        me2side1 = me2side1_.replace("_", " ")
        me2side2_ = str(self.get_cookie("me2-side2"))
        me2side2 = me2side2_.replace("_", " ")
        pa2name_ = str(self.get_cookie("pa2-name"))
        pa2name = pa2name_.replace("_", " ")

        items = [
            [me0main,
             me0side0,
             me0side1,
             me0side2,
             pa0name,
             str(self.get_cookie("pa0-duration"))],
            [me1main,
             me1side0,
             me1side1,
             me1side2,
             pa1name,
             str(self.get_cookie("pa1-duration"))],
            [me2main,
             me2side0,
             me2side1,
             me2side2,
             pa2name,
             str(self.get_cookie("pa2-duration"))]
        ]

        self.render("templates/pages/recommendations.html", items=items)

        return

    def post(self):

        recommendation_0_meal_feedback = str(self.get_body_argument("rec0-meal", ""))
        recommendation_0_pa_feedback = str(self.get_body_argument("rec0-pa", ""))

        if str(self.get_body_argument("favorite-0", "")) == 'on':

            recommendation_0_favorite = "1"

        else:

            recommendation_0_favorite = "0"

        self.set_cookie("re0-meal-fe", recommendation_0_meal_feedback, expires_days=1, httponly=True)
        self.set_cookie("re0-pa-fe", recommendation_0_pa_feedback, expires_days=1, httponly=True)
        self.set_cookie("re0-fav", recommendation_0_favorite, expires_days=1, httponly=True)

        recommendation_1_meal_feedback = str(self.get_body_argument("rec1-meal", ""))
        recommendation_1_pa_feedback = str(self.get_body_argument("rec1-pa", ""))

        if str(self.get_body_argument("favorite-1", "")) == 'on':

            recommendation_1_favorite = "1"

        else:

            recommendation_1_favorite = "0"

        self.set_cookie("re1-meal-fe", recommendation_1_meal_feedback, expires_days=1, httponly=True)
        self.set_cookie("re1-pa-fe", recommendation_1_pa_feedback, expires_days=1, httponly=True)
        self.set_cookie("re1-fav", recommendation_1_favorite, expires_days=1, httponly=True)

        recommendation_2_meal_feedback = str(self.get_body_argument("rec2-meal", ""))
        recommendation_2_pa_feedback = str(self.get_body_argument("rec2-pa", ""))

        if str(self.get_body_argument("favorite-2", "")) == 'on':

            recommendation_2_favorite = "1"

        else:

            recommendation_2_favorite = "0"

        self.set_cookie("re2-meal-fe", recommendation_2_meal_feedback, expires_days=1, httponly=True)
        self.set_cookie("re2-pa-fe", recommendation_2_pa_feedback, expires_days=1, httponly=True)
        self.set_cookie("re2-fav", recommendation_2_favorite, expires_days=1, httponly=True)

        self.redirect("/feedback")

        return


# This class loads either the last stage of the workflow if the user say "No" or it redirects the user to and extra
# stage if user say "Yes".
class Feedback(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/feedback.html")

        return

    def post(self):

        answer = str(self.get_body_argument("feedback"))

        if answer == "No":

            # This object stores in the database the user feedback. It only considers bundles.
            fc = FeedbackConnection()
            fc.store_bundles_feedback(int(self.get_cookie("unanswered")),
                                      int(self.get_cookie("re0-meal-fe")),
                                      int(self.get_cookie("re0-pa-fe")),
                                      int(self.get_cookie("re0-fav")),
                                      int(self.get_cookie("re1-meal-fe")),
                                      int(self.get_cookie("re1-pa-fe")),
                                      int(self.get_cookie("re1-fav")),
                                      int(self.get_cookie("re2-meal-fe")),
                                      int(self.get_cookie("re2-pa-fe")),
                                      int(self.get_cookie("re2-fav")))

            self.redirect("/finish")

            return

        else:

            self.redirect("/form")

            return


# This class loads an extra stage where we ask about 4 aspects of the recommendations: diversity, level of surprise,
# reliability and healthiness.
class Form(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/form.html")

        return

    def post(self):

        diversity_feedback = int(self.get_body_argument("diversity", ""))
        surprising_feedback = int(self.get_body_argument("surprising", ""))
        reliability_feedback = int(self.get_body_argument("reliability", ""))
        healthy_feedback = int(self.get_body_argument("healthy", ""))

        # This object stores in the database the user feedback. It considers both bundles and the four metrics.
        fc = FeedbackConnection()
        fc.store_full_feedback(int(self.get_cookie("unanswered")),
                               int(self.get_cookie("re0-meal-fe")),
                               int(self.get_cookie("re0-pa-fe")),
                               int(self.get_cookie("re0-fav")),
                               int(self.get_cookie("re1-meal-fe")),
                               int(self.get_cookie("re1-pa-fe")),
                               int(self.get_cookie("re1-fav")),
                               int(self.get_cookie("re2-meal-fe")),
                               int(self.get_cookie("re2-pa-fe")),
                               int(self.get_cookie("re2-fav")),
                               diversity_feedback, surprising_feedback, reliability_feedback, healthy_feedback)

        self.redirect("/finish")


# This class loads the page where EvoRecSys says: "Thank you and bye".
class Finish(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/finish.html")

        return

    def post(self):

        self.clear_all_cookies("/")
        self.clear_all_cookies()
        self.redirect("/")
        self.on_connection_close()

        return


# This class loads a page where the user is notified that their web browser doesn't allow us to use cookies.
class NoCookies(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/no-cookies.html")

        return

    def post(self):

        self.clear_all_cookies()
        self.redirect("/")
        self.on_connection_close()

        return

# This class loads a page where the user is notified if an internal error has occurred.
class Errors(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.redirect("/error")

        return

    def get(self):

        self.render("templates/pages/error.html")

        return

    def post(self):

        self.clear_all_cookies()
        self.redirect("/")
        self.on_connection_close()

        return


# We create all the pages of our web app.
def make_app():

    settings = {"static_path": os.path.join(os.path.dirname(__file__), "templates")}
    handlers = [(r"/", IndexEvoRecSys), (r"/start", Start), (r"/physical-I", PhysicalDataI),
                (r"/physical-II", PhysicalDataII), (r"/physical-III", PhysicalDataIII), (r"/food-I", FoodDataI),
                (r"/food-II", FoodDataII), (r"/food-III", FoodDataIII), (r"/food-IV", FoodDataIV),
                (r"/food-V", FoodDataV), (r"/exercising-I", ExercisingDataI), (r"/exercising-II", ExercisingDataII),
                (r"/exercising-III", ExercisingDataIII), (r"/exercising-IV", ExercisingDataIV), (r"/goal", GoalData),
                (r"/process-data", ProcessData), (r"/recommendations", Recommendations), (r"/feedback", Feedback),
                (r"/form", Form), (r"/finish", Finish), (r"/no-cookies", NoCookies), (r"/error", Errors)]

    app = tornado.web.Application(handlers, **settings, autoreload=True)

    return app


# We deploy our EvoRecSys web app. It uses port 8081 to receive requests. The IP is localhost.
if __name__ == '__main__':

    col_evo_rec_sys = make_app()
    col_evo_rec_sys.listen(8081)
    tornado.ioloop.IOLoop.instance().start()

