# Indexit

Indexit allows you to scrape Github and index every (public) repository and its code. You can then run better queries on the code, like regex.

<img src="https://i.imgur.com/8oGzPY6.png">

### Installation

- ``` git pull https://github.com/filtration/indexit.git ```
- ``` sudo chmod +x install.sh  ```
- ``` . ./install.sh ```
- ``` cp config.example.yml config.yml ```
- ``` python ./indexit.py  ```

### Why?

Well, indexit can index about a million files every 10 minutes or so (once refactored it will be more), and this will give us the option to regex search code to find credentials/passwords or anything else.

### Todo

- Better rate limit checking/management.
- Speed up git clone
- Once indexed, check for updated code