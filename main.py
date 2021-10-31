import os
import asyncio
from dotenv import load_dotenv
from snow_connector import MakeSnowConnection, MakeAsyncSnowConnection
from snow_connector.faker_filler import return_fake_inc_body



if __name__ == "__main__":
    load_dotenv()
    base_url = os.getenv('BASE_URL')
    snow_usr = os.getenv('SNOW_USR')
    snow_pwd = os.getenv('SNOW_PWD')
    body = return_fake_inc_body()
    connection_obj = MakeAsyncSnowConnection(base_url, snow_usr, snow_pwd)
    asyncio.run(connection_obj.post_single_inc_async(body,1))

