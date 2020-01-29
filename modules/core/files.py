import os
from modules.core.database import Database
from config.files import Files as FilesConfig

class Files:

    # Files constructor
    def __init__(self):
        self.connection = Database()
        self.file_config = FilesConfig()

    # Get the contents of the file and index it
    def contents(self, name):
        # Our blacklisted extensions and folders
        exclude_extensions = set(self.file_config.blacklisted_extensions())
        exclude_dirs = set(self.file_config.blacklisted_dirs())

        # Get all the files/folders minus the blacklisted ones
        for root, dirs, files in os.walk("/tmp/indexit/git/%s" % name, topdown=True):

            # Remove blacklisted files/folders
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            files[:] = [f for f in files if f not in exclude_extensions]
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



