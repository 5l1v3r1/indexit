import os
from modules.core.database import Database
from config.files import Files as FilesConfig


class Files:

    # Files constructor
    def __init__(self):
        self.connection = Database()
        self.file_config = FilesConfig()

    # Get the contents of the file and index it
    def contents(self, repo):
        # Our blacklisted extensions and folders
        exclude_extensions = set(self.file_config.blacklisted_extensions())
        exclude_dirs = set(self.file_config.blacklisted_dirs())

        # Get all the files/folders minus the blacklisted ones
        for root, dirs, files in os.walk("/tmp/indexit/git/%s" % repo['name'], topdown=True):

            # Remove blacklisted files/folders
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            files[:] = [f for f in files if f not in exclude_extensions]
            for file in files:
                try:
                    # Remove full temp path and repo name from file path
                    tmp_location = "%s/%s" % (root, file)
                    location = tmp_location.replace('/tmp/indexit/git/%s/' % repo['name'], '')

                    # Open the file and save the contents
                    with open('%s/%s' % (root, file)) as f:
                        payload = {
                            'repo_id': repo['id'],
                            'name': repo['name'],
                            'commit_id': repo['commit_id'],
                            'file': location,
                            'content': f.read()
                        }
                        self.save(payload)
                except:
                    break

    # Save file to database
    def save(self, payload):
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
        data = (
            payload['repo_id'],
            payload['name'],
            payload['file'],
            payload['content'],
            payload['commit_id']
        )

        try:
            with self.connection.get() as connection:
                cur = connection.cursor()
                cur.execute(sql, data)
        except Exception as e:
            print(e)



