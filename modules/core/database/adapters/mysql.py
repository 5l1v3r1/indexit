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
        try:
            cur = self.database.cursor()
            cur.executemany(sql, files)
            self.database.commit()
        except Exception as e:
            print("error", e)

    # Mysql constructor
    def initialize(self):
        createContents = """
            CREATE TABLE IF NOT EXISTS contents(
                `id` int unsigned NOT NULL AUTO_INCREMENT,
                `repo_id` int DEFAULT NULL,
                `name` TEXT,
                `file` TEXT,
                `content` LONGTEXT,
                `commit_id` varchar(60) DEFAULT NULL,
                `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"""

        self.get().cursor().execute(createContents)