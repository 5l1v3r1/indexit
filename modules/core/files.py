import os


class Files:

    # Get the contents of the file and index it
    def contents(self, name):
        for root, dirs, files in os.walk("/tmp/indexit/git/%s" % name):
            for file in files:
                try:
                    with open('%s/%s' % (root, file)) as f:
                        print(f.read()) # store to database
                except:
                    break
