from decouple import config
from create_app import CreateApp

#constants
def generalAuth(data: dict):
    CreateApp(config_var=data)
    return {
        "status": "sucessful",
        "name": CreateApp.get_app_name()
    }

