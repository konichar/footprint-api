import re
import heroku3
from decouple import config

API_KEY = config('API_KEY')

class CreateApp:
    """Class to perform """
    def __init__(self, app_name:str, github_link: str, session: str) -> None:
        self.heroku_name = heroku3.from_key(API_KEY)
        self.__createApp(app_name)
        self.__config(session)
        

    def __createApp(self, app_name):
        name_regex = re.compile(r"^[a-z][a-z0-9]{1,28}[a-z0-9]$")
        if name_regex.search(app_name) is None:
            raise ValueError(
                "Improper name configuration. Names must begin with an alphabet, can consist of numbers and hyphens as seperators."
            )
        self.app = self.heroku_name.create_app(name=app_name)
        return
    
    def __config(self, config):
        self.config_vars = self.app.config()
        self.config_vars['SESSION'] = config

    def __connectGithub(self, url):
        pass

def main():
    heroku_conn = heroku3.from_key(API_KEY)
    print(heroku_conn.apps())
