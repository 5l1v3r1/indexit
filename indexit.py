from multiprocessing import Pool
from modules.github.repositories import Repositories
from modules.core.git import Git
from modules.core.files import Files
from modules.core.database.database import Database
from config.threads import Threads
import yappi

logo = f"""
{'#' * 69}
#                                                                   #
# Indexit: Created by @Filtration                                   #
#                                                                   #
# Indexit stores github repos in the database for better searches   #
#                                                                   #
{'#' * 69}
"""


class Indexit:

    # Indexit constructor
    def __init__(self):
        self.repositories = Repositories()
        self.git = Git()
        self.files = Files()

    # Get the repo
    def run(self, repo_id):
        # initiate database
        database = Database.connect()

        # Don't run if already indexed
        if self.repositories.indexed(repo_id):
            return

        # Get the repo information
        uri = "https://api.github.com/repositories/%d" % repo_id
        repository = self.repositories.get(uri)

        # Clone the repo
        if 'html_url' in repository:
            clone = self.git.clone(
                repository['full_name'],
                repository['html_url'],
                repo_id
            )

            # Run through files and store contents
            files = self.files.contents(clone)

            # Save files to database
            Database.save(database, files)

            # Delete repo in temp folder
            self.repositories.delete(repository['full_name'])

            print('Indexed ', uri)


    # Index threading
    def main(self):
        yappi.start()
        # Pool connections to speed up our job
        # with Pool(processes=Threads().total()) as pool:
        #     pool.map(self.run, range(30))

        for i in range(100):
            self.run(i)
        yappi.get_func_stats().print_all()
        yappi.get_thread_stats().print_all()


# Indexit logo
print(logo)

# Let's go!
Indexit().main()

