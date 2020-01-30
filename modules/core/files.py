import os, json
from config.files import Files as FilesConfig


class Files:

    # Files constructor
    def __init__(self):
        self.files = []
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
                    with open('%s/%s' % (root, file), 'r', encoding='latin-1') as f:
                        self.files.append((
                            repo['id'],
                            repo['name'],
                            location,
                            f.read(),
                            repo['commit_id']
                        ))
                except Exception as e:
                    print(e)
                    break

        # Save all files
        return self.files



