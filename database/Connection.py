# This is an abstract class. It is used to create the three connection objects used in the full workflow of
# EvoRecSys.
class Connection:

    # These values should be changed according to your network configurations.
    HOST = '192.168.X.X'  
    USER = 'misterious_guy'
    PASSWORD = 'hiddenLetters'
    DATA_BASE = 'evo_rec_sys'

    # Constructor
    def __init__(self):

        self.connector = None
