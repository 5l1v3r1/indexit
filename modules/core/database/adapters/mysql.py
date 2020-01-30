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
            except Exception as e:
                self.database.rollback()
                print("error %s" % e)
            else:
                break

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