import sqlite3
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from config.database import Database as Config
from modules.core.database.adapters.sqlite import Sqlite
from modules.core.database.adapters.mysql import Mysql


class Database:

    # Save file to adapters
    @staticmethod
    def save(database, files):
        if Config().type() == 'sqlite':
            Sqlite(database).save(files)
        elif Config().type() == 'mysql':
            Mysql(database).save(files)

    # Connect to the database
    @staticmethod
    def connect():
        if Config().type() == 'mysql':
            return mysql.connector.pooling.MySQLConnectionPool(**Config().mysql())
        elif Config().type() == 'sqlite':
            return sqlite3.connect("%s.sqlite" % Config().sqlite())
