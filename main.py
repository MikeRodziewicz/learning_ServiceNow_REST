import asyncio
import aiohttp
from threading import Thread
import time
import os
import json
from dotenv import load_dotenv

from snow_connector import MakeSnowConnection
from snow_connector.faker_filler import return_fake_inc_body


# def send_async_request(connection_obj, sysparm_limit, sysparm_query):
#     return connection_obj.get_multiple_incident(sysparm_limit, sysparm_query)

# def main(sysparm_limit, sysparm_query):
#     load_dotenv()
#     # time.sleep(3)
#     base_url = os.getenv('BASE_URL')
#     snow_usr = os.getenv('SNOW_USR')
#     snow_pwd = os.getenv('SNOW_PWD')
#     connection_obj = MakeSnowConnection(base_url, snow_usr, snow_pwd)
#     thr = Thread(target=send_async_request, args=[connection_obj, sysparm_limit, sysparm_query])
#     thr.start()
#     return thr


async def log_multiple_incidents(how_many_times:int, connection: object):
    effects = []
    async with aiohttp.ClientSession() as session:
        for _ in range(how_many_times):
            body = return_fake_inc_body()
            time.sleep(0.01)
            response = await session.connection_obj.post_single_incident(body)
            print(response.reason)
            effects.append(await response.json())
            print(response)
    return effects

    

if __name__ == "__main__":
    load_dotenv()
    base_url = os.getenv('BASE_URL')
    snow_usr = os.getenv('SNOW_USR')
    snow_pwd = os.getenv('SNOW_PWD')
    connection_obj = MakeSnowConnection(base_url, snow_usr, snow_pwd)
    asyncio.run(log_multiple_incidents(2, connection=connection_obj))