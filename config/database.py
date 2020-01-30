from modules.core.config import *


class Database:

    # Get the adapters type
    @staticmethod
    def type():
        return config['DATABASE']['type']

    # Get the mysql config
    @staticmethod
    def mysql():
        return {
            'user': config['DATABASE']['mysql']['user'],
            'password': config['DATABASE']['mysql']['password'],
            'host': config['DATABASE']['mysql']['host'],
            'database': config['DATABASE']['mysql']['database'],
            'auth_plugin': 'mysql_native_password'
        }

    # Sqlite connection
    @staticmethod
    def sqlite():
        return '%s.sqlite' % config['DATABASE']['sqlite']
