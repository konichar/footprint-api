from heroku_py.heroku_client import HerokuClient
import re
from heroku_py.heroku_client import HerokuClient
from decouple import config

#constants
API_KEY = config('API_KEY')


class CreateApp:
    """Class to perform """
    def __init__(self, app_name:str, github_link: str, session: str) -> None:
        self.heroku = HerokuClient(api_key=API_KEY)
        self.heroku.create_app(app_name=app_name)
        self.heroku.build_from_git(app_name_or_id=app_name, git_url=github_link)
        

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
