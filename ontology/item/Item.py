# This is an abstract class. It is used to create both food item and physical activity objects.
class Item:

    # Constructor
    def __init__(self, name, category):

        self.name = name
        self.category = category
