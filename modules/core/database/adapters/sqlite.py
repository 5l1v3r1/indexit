class Sqlite:

    # Sqlite constructor
    def __init__(self, database):
        self.database = database

    # Save to sqlite database
    def save(self, files):
        sql = """
            INSERT INTO contents(
                repo_id,
                name,
                file,
                content,
                commit_id
            )
            VALUES(?, ?, ?, ?, ?)
        """
        sqlite = Sqlite()
        database = sqlite.get()
        try:
            with database as connection:
                connection.executemany(sql, files)
        except Exception as e:
            print(e)

    # Create the table structure
    def initialize(self):
        createContents = """
            CREATE TABLE IF NOT EXISTS contents(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                repo_id INTEGER,
                name varchar(32), 
                file varchar(32), 
                content TEXT,
                commit_id varchar(60),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        self.get().cursor().execute(createContents)
