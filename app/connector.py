
import os
import requests

class DevConfig:
    BASE_URL = os.environ.get('SNOW_BASE_DEV_URL')
    USER =  os.environ.get('SNOW_DEV_USER')
    PWD = os.environ.get('SNOW_DEV_PWD')


class TestConfig:
    BASE_URL = os.environ.get('SNOW_BASE_TEST_URL')
    USER =  os.environ.get('SNOW_TEST_USER')
    PWD = os.environ.get('SNOW_TEST_PWD')


class ProdConfig:
    BASE_URL = os.environ.get('SNOW_BASE_PROD_URL')
    USER =  os.environ.get('SNOW_PROD_USER')
    PWD = os.environ.get('SNOW_PROD_PWD')


class PDIConfig:
    BASE_URL = os.environ.get('SNOW_PDI_URL')
    USER =  os.environ.get('SNOW_PDI_USER') or 'test'
    PWD = os.environ.get('SNOW_PDI_PWD') 

config = {
    'pdi': PDIConfig,
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
    'default': PDIConfig
}   


class Foo():

    def __init__(self, env) -> None:
        self.baseUrl = env.BASE_URL
        self.username = env.USER
        self.password = env.PWD

    def __str__(self) -> str:
        return f'this is the username: {self.username}, and this is the baseURL {self.baseUrl}'

    def make_connection(self):
        conn = requests.get(self.baseUrl, auth=(self.username, self.password)) #missing headers and body
        data = conn.json()
        return data


def get_the_config():
    env = os.environ.get('ENV')
    return config[env]



# payload = {
#     'sysparm_query' : f'sysparm_query={sysparm_query}',
#     'sysparm_limit' : f'sysparm_limit={sysparm_limit}',
#     'sysparm_display_value' : f'sysparm_display_value={sysparm_display_value}',
#     'sysparm_fields' : f'sysparm_fields={sysparm_fields}'
# }





