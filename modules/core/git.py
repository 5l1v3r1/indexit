import os
from git import Repo


class Git:

    # Clone the repository
    def clone(self, name, url, id):
        # Location where we are cloning the repo
        location = '/tmp/indexit/git/%s' % name

        # Clone the repo and checkout
        try:
            # Make sure repo doesn't exist
            if os.path.exists(location):
                repo = Repo(location)
            else:
                args = {
                    'single-branch': True,
                    'no-tags': True,
                    'depth': 1
                }
                repo = Repo.clone_from(url, location, **args)
        except Exception as e:
            return
        else:
            # Return the commit ID
            try:
                return {
                    'id': id,
                    'name': name,
                    'commit_id': repo.head.object.hexsha
                }
            except:
                return
