# This is an abstract class. It is used to create the three connection objects used in the full workflow of
# EvoRecSys.
class Connection:

    # These values should be changed according to your network configurations.
    HOST = '192.168.X.X'  # '172.20.10.13'
    USER = 'hugo'
    PASSWORD = 'hugo12345'
    DATA_BASE = 'evo_rec_sys'

    # Constructor
    def __init__(self):

        self.connector = None
