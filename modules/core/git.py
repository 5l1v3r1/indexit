from git import Repo


class Git:

    # Clone the repository
    def clone(self, name, url, id):
        # Location where we are cloning the repo
        location = '/tmp/indexit/git/%s' % name

        # Clone the repo and checkout
        try:
            repo = Repo.clone_from(url, location)
            repo.heads['master'].checkout()
        except Exception as e:
            return
        else:
            # Return the commit ID
            return {
                'id': id,
                'name': name,
                'commit_id': repo.head.object.hexsha
            }
