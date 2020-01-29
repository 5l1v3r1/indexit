import os
from modules.core.database import Database


class Files:

    # Files constructor
    def __init__(self):
        self.connection = Database()

    # Get the contents of the file and index it
    def contents(self, name):
        for root, dirs, files in os.walk("/tmp/indexit/git/%s" % name):
            for file in files:
                try:
                    with open('%s/%s' % (root, file)) as f:
                        self.save(f.read())
                except:
                    break

    # Save file to database
    def save(self, content):
        sql = """
            INSERT INTO contents(
                name,
                content,
                commit_id
            )
            VALUES(?, ?, ?)
        """
        data = ('rep name', content, '1234')

        try:
            with self.connection.get() as connection:
                cur = connection.cursor()
                print(cur)
                cur.execute(sql, data)
        except Exception as e:
            print(e)



