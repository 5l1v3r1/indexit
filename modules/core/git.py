import os


class Git:

    # Clone the repository
    def clone(self, name, url):
        os.system("git clone --single-branch --no-tags --depth 1 %s /tmp/indexit/git/%s > /dev/null 2>&1" % (url, name))
