import os
import json
from dotenv import load_dotenv

from snow_connector import MakeSnowConnection
from snow_connector.faker_filler import return_fake_inc_body


def main(how_many_times: int, connection_obj: object):
    for _ in range(how_many_times):
        body = return_fake_inc_body()
        print(body)
        response = connection_obj.post_single_incident(body)
        # print(response.reason)
        print(json.dumps(response))


if __name__ == "__main__":
    load_dotenv()
    base_url = os.getenv('BASE_URL')
    snow_usr = os.getenv('SNOW_USR')
    snow_pwd = os.getenv('SNOW_PWD')
    connection_obj = MakeSnowConnection(base_url, snow_usr, snow_pwd)
    # print(connection_obj.get_all_emails(2))
    print(connection_obj.get_single_email('026ba8f21b32301064fc43fddc4bcb4a'))
    # main(1,connection_obj)
    
  
