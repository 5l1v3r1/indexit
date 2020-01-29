import os, json, requests
from config.github import Github as GithubConfig


class Repositories:

    # Get the repository
    def get(self, uri):
        # For api keys, exit if success
        for token in GithubConfig().tokens():
            try:
                with requests.get(uri, headers={'Authorization': 'token %s' % token}) as response:
                    data = json.loads(response.text)
                    if 'message' in data and 'API rate limit' in data['message']:
                        print("rate limit hit, retrying...")
                    if 'message' in data and 'Bad credentials' in data['message']:
                        print("Your credentials are wrong!!")
                    else:
                        return data
            except:
                return

    # Delete repo files on system
    def delete(self, name):
        os.system("rm -rf /tmp/indexit/git/%s" % name)

    # Already indexed?
    def indexed(self, name):
        # db: identifier = github id in url
        return False