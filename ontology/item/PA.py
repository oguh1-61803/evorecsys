# All necessary imports from other files.
from src.ontology.item.Item import Item


# This class instant represents a physical activity item. It contains numerous characteristics, intensity and a specific
# duration. It extends from the Item class.
class PA(Item):

    # Constructor
    def __init__(self, name, category, indoors, outdoors, intensity, met, duration=-1):

        super().__init__(name, category)

        self.indoors = indoors
        self.outdoors = outdoors
        self.intensity = intensity
        self.met = met
        self.duration = duration
