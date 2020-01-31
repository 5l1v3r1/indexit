class Mysql:

    # Mysql constructor
    def __init__(self, database):
        self.database = database

    # Save to the database
    def save(self, files):
        sql = """
            INSERT INTO contents(
                repo_id,
                name,
                file,
                content,
                commit_id
            )
            VALUES(%s, %s, %s, %s, %s)
        """
        for attempt in range(20):
            try:
                cur = self.database.cursor()
                cur.executemany(sql, files)
                self.database.commit()
            except:
                pass
            else:
                break

    # Add repo to indexed
    def indexed(self, repo_id):
        sql = """
            INSERT INTO repositories(repo_id)
            VALUES(%s)
        """
        for attempt in range(20):
            try:
                cur = self.database.cursor()
                cur.execute(sql, (repo_id,))
                self.database.commit()
            except:
                pass
            else:
                break

    # Already indexed?
    def has_been_indexed(self, repo_id):
        sql = """
            SELECT repo_id FROM repositories
            WHERE repo_id = %s
            LIMIT 1
        """
        for attempt in range(5):
            try:
                cur = self.database.cursor()
                cur.execute(sql, (repo_id, ))
                indexed = cur.fetchall()
            except Exception as e:
                pass
            else:
                if not indexed:
                    return False
                return True

    # Mysql constructor
    def initialize(self):
        """
        Not a script kiddie? You know what to change this to
        to speed up the indexing, but let's not put the food directly
        in to their mouths.
        """
        createContents = """
            CREATE TABLE IF NOT EXISTS contents(
                `repo_id` int DEFAULT NULL,
                `name` TEXT,
                `file` TEXT,
                `content` LONGTEXT,
                `commit_id` varchar(60) DEFAULT NULL,
                `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"""

        self.get().cursor().execute(createContents)