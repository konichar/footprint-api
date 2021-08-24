import random
from heroku_py.heroku_client import HerokuClient
from decouple import config

class CreateApp:

    NAME: str = 'footprint'

    def __init__(self, config_var:dict) -> None:
        """
            Create a new heroku forwarder application

            App constructor requiring no user name, github link and api_key

            application name is generated at random
            github link is default
            api_key is the default:
                this means the applicaiton is created under the developers account
        """        
        self.app_name = self.__generate_name()
        self.api_key = config('API_KEY')
        self.github_link = config('GIT_URL')
        self.config_var = config_var

        self.heroku = HerokuClient(api_key=self.api_key)
        self.heroku.create_app(app_name=self.app_name)
        self.heroku.build_from_git(app_name_or_id=self.app_name, git_url=self.github_link)
        self.heroku.create_config(app_name_or_id=self.app_name, config_vars= config_var)
    
    def __init__(self, api_key: str, config_var:dict) -> None:
        """
            Create a new heroku forwarder application

            App constructor requiring no user name, and github link

            application name is generated at random
            github link is default
            api_key sets up the application on the end user account
        """        
        self.app_name = self.__generate_name()
        self.api_key = api_key
        self.github_link = config('GIT_URL')
        self.config_var = config_var

        self.heroku = HerokuClient(api_key=api_key)
        self.heroku.create_app(app_name=self.app_name)
        self.heroku.build_from_git(app_name_or_id=self.app_name, git_url=self.github_link)
        self.heroku.create_config(app_name_or_id=self.app_name, config_vars= config_var)
    

    def __init__(self, app_name:str, api_key: str, github_link: str, config_var:dict) -> None:
        """
            Create a new heroku forwarder application
        
            Constructor requiring all field entries

            app_name is the name of the applicaiton on heroku
            github_link is the source code from which the application would run
        """        
        self.app_name = app_name
        self.api_key = api_key
        self.github_link = github_link
        self.config_var = config_var

        self.heroku = HerokuClient(api_key=api_key)
        self.heroku.create_app(app_name=app_name)
        self.heroku.build_from_git(app_name_or_id=app_name, git_url=github_link)
        self.heroku.create_config(app_name_or_id=app_name, config_vars= config_var)
    

    def __generate_name(self)->str:
        """
            This is a private function that generates application name for each user

            This helps to abstract the whole app creation process as much as possible
            This function creates a random 8 digit name comprising of shuffled letters and alphabets
            this is a private funtion
        """ 
        _alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        _numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9','_']
        _name = list()
        for l in range(4):
            _name.append(random.choice(_alphabets))
            _numbers.append(random.choice(_numbers))

        random.shuffle(_name)
        return self.NAME.join(_name)


    def get_app_name(self):
        """
            Returns String

            the name of the application is returned
        """
        return self.app_name
    
    def get_github_link(self):
        """
            Returns String

            the url of the source code of the running application is returned
        """
        return self.github_link
    
    def get_config_vars(self):
        """
            Returns dict

            a dictionary of the config variables is returned
        """
        return self.session_str
