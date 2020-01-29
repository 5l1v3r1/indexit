import os
from modules.core.database import Database


class Files:

    # Files constructor
    def __init__(self):
        self.connection = Database()

    # Get the contents of the file and index it
    def contents(self, name):
        exclude_files = set(['.exe', '.png', '.jpg', '.zip', '.rar'])
        exclude_dirs = set(['.git'])
        for root, dirs, files in os.walk("/tmp/indexit/git/%s" % name):
            files[:] = [f for f in files if f not in exclude_files]
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                try:
                    with open('%s/%s' % (root, file)) as f:
                        payload = {
                            'name': name,
                            'file': "%s/%s" % (name, file),
                            'content': f.read()
                        }
                        self.save(payload)
                except:
                    break

    # Save file to database
    def save(self, payload):
        sql = """
            INSERT INTO contents(
                name,
                file,
                content,
                commit_id
            )
            VALUES(?, ?, ?, ?)
        """
        data = (payload['name'], payload['file'], payload['content'], '1234')

        try:
            with self.connection.get() as connection:
                cur = connection.cursor()
                cur.execute(sql, data)
        except Exception as e:
            print(e)



