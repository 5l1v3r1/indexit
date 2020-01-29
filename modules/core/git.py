from git import Repo
import os


class Git:

    # Clone the repository
    def clone(self, name, url, id):
        # Location where we are cloning the repo
        location = '/tmp/indexit/git/%s' % name

        # Clone the repo and checkout
        try:
            os.system("git clone --single-branch --no-tags --depth 1 %s /tmp/indexit/git/%s > /dev/null 2>&1" % (
                url, name
            ))
            repo = os.system("git -C %s rev-parse HEAD > /dev/null 2>&1" % location)
            # repo = Repo.clone_from(url, location)
            # repo.heads['master'].checkout()
        except Exception as e:
            return
        else:
            # Return the commit ID
            return {
                'id': id,
                'name': name,
                'commit_id': repo
            }
