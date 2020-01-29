from modules.core.config import *


class Files:

    # Blacklisted dirs
    def blacklisted_dirs(self):
        return config['FILES']['blacklisted_dirs']

    # Blacklisted dirs
    def blacklisted_extensions(self):
        return config['FILES']['blacklisted_extensions']
