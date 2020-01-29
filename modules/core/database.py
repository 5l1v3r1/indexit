import sqlite3
from config.database import Database as Config


class Database:

    # Connect to the database
    def __init__(self):
        self.initalize()

    # Return the instance
    def get(self):
        return sqlite3.connect(Config().name())

    # Create the table structure
    def initalize(self):
        createContents = """
            CREATE TABLE IF NOT EXISTS contents(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                repo_id INTEGER,
                name varchar(32), 
                file varchar(32), 
                content TEXT,
                commit_id varchar(32),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        self.get().cursor().execute(createContents)