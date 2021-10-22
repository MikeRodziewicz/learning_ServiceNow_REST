import os
import random
from dotenv import load_dotenv

from snow_connector import MakeSnowConnection
from snow_connector.faker_filler import return_fake_inc_body


load_dotenv()

base_url = os.getenv('BASE_URL')
snow_usr = os.getenv('SNOW_USR')
snow_pwd = os.getenv('SNOW_PWD')

def main(how_many_times: int, connection_obj: object):
    pass

if __name__ == "__main__":
    connection_obj = MakeSnowConnection(base_url, snow_usr, snow_pwd)
    main(10,connection_obj)
    
  
