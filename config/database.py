from modules.core.config import *


class Database:

    # Get the database name
    def name(self):
        return "%s.sqlite" % config['DATABASE']['name']

