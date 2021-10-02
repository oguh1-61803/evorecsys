# This is an abstract class. It is used to create the three connection objects used in the full workflow of
# EvoRecSys.
class Connection:

    # These values should be changed according to your network configurations.
    HOST = '192.168.0.30'  # '172.20.10.13'
    USER = 'root'
    PASSWORD = 'hola123'
    DATA_BASE = 'evo_rec_sys_v2'

    # Constructor
    def __init__(self):

        self.connector = None
