from threading import Thread
import time
import os
import json
from dotenv import load_dotenv

from snow_connector import MakeSnowConnection
from snow_connector.faker_filler import return_fake_inc_body


def send_async_request(connection_obj, sysparm_limit, sysparm_query):
    return connection_obj.get_multiple_incident(sysparm_limit, sysparm_query)

def main(sysparm_limit, sysparm_query):
    load_dotenv()
    # time.sleep(3)
    base_url = os.getenv('BASE_URL')
    snow_usr = os.getenv('SNOW_USR')
    snow_pwd = os.getenv('SNOW_PWD')
    connection_obj = MakeSnowConnection(base_url, snow_usr, snow_pwd)
    thr = Thread(target=send_async_request, args=[connection_obj, sysparm_limit, sysparm_query])
    thr.start()
    return thr
# def main(how_many_times: int, connection_obj: object):
#     for _ in range(how_many_times):
#         body = return_fake_inc_body()
#         print(body)
#         response = connection_obj.post_single_incident(body)
#         # print(response.reason)
#         print(json.dumps(response))
# date_to_use = '2021-10-23 08:37:31'
# data = {
#     'sysparm_limit': "1",
#     'sysparm_query': f'sys_created_on>="2021-10-23 08:37:31"'
# }
# print(connection_obj.get_multiple_emails(sysparm_limit=1, sysparm_query='sys_created_on>="2021-10-25 08:37:31"'))
# response = connection_obj.get_multiple_incident()
# print(response['result'][0])
# print(response.status_code)
# print(response.request)
# response = response.json()
# print(len(response['result']))

if __name__ == "__main__":
    start = time.time()
    print(main(sysparm_limit=20,sysparm_query=None))
    end = time.time()
    total_time = end - start
    print("this is total time", total_time)
    # load_dotenv()
    # base_url = os.getenv('BASE_URL')
    # snow_usr = os.getenv('SNOW_USR')
    # snow_pwd = os.getenv('SNOW_PWD')
    # connection_obj = MakeSnowConnection(base_url, snow_usr, snow_pwd)
    # start = time.time()
    # print(connection_obj.get_multiple_incident(sysparm_limit=20, sysparm_query=None))
    # end = time.time()
    # total_time = end - start
    # print("this is total time", total_time)
