import requests
import os
import asyncio
import aiohttp
from dotenv import load_dotenv
from faker_filler import return_fake_inc_body
import json

class MakeSnowConnection():

    def __init__(self, base_url, user, password) -> None:
        self.baseUrl = base_url
        self.username = user
        self.password = password
        self.payload = None
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def _make_connection(self, method, url, **kwargs): 
        try: 
            self.response = requests.request(auth=(self.username, self.password), method=method, url=url, headers=self.headers, json=self.payload, **kwargs)
            print(self.response.url)
            print(self.response)
            print(type(self.response))
            # self.response = self.response.json()
            return self.response
        except requests.exceptions.HTTPError as errh:
            print(errh)

    def get_single_incident(self, inc_number: str):
        method = "GET"
        url = f"{self.baseUrl}/api/now/table/incident?sysparm_query=number={inc_number}"
        return self._make_connection(method, url)

    def get_multiple_incident(self, sysparm_limit="1", sysparm_query=None):
        method = "GET"
        url = f"{self.baseUrl}/api/now/table/incident?sysparm_limit={sysparm_limit}&sysparm_query={sysparm_query}"
        return self._make_connection(method, url)

    def post_single_incident(self, body: dict):
        method = "POST"
        self.payload = body
        url = f"{self.baseUrl}/api/now/table/incident"
        return self._make_connection(method, url)

    def get_multiple_emails(self, sysparm_limit="1", sysparm_query=None):
        method = "GET"
        url = f"{self.baseUrl}/api/now/table/sys_email?sysparm_limit={sysparm_limit}&sysparm_query={sysparm_query}"
        return self._make_connection(method, url)
        
    def get_single_email(self, sys_id:str):
        method = "GET"
        url = f"{self.baseUrl}/api/now/v1/email/{sys_id}"
        return self._make_connection(method, url)

class MakeAsyncSnowConnection():

    def __init__(self, base_url, user, password) -> None:
        self.baseUrl = base_url
        self.username = user
        self.password = password
        self.payload = None
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def _get_tasks(self, session, url, method, how_many=1):
        tasks = []
        for _ in range(how_many):
            try:
                tasks.append(asyncio.create_task(session.request(url=url, method=method, auth=aiohttp.BasicAuth(self.username, self.password), data=self.payload, headers=self.headers)))
            except:
                passs
        return tasks

    async def _make_connection(self, method, url, how_many):
        outcome = []
        async with aiohttp.ClientSession() as session:
            tasks = self._get_tasks(session, url, method, how_many)
            responses = await asyncio.ensure_future(asyncio.gather(*tasks))
            for response in responses:
                outcome.append(await response.json())
            return outcome

    async def post_single_inc_async(self, body:dict, how_many):
        method = "POST"
        self.payload = json.dumps(body)
        url = f"{self.baseUrl}/api/now/table/incident"
        outcome = await self._make_connection(method, url, how_many)
        return outcome

if __name__ == "__main__":
    load_dotenv()
    base_url = os.getenv('BASE_URL')
    snow_usr = os.getenv('SNOW_USR')
    snow_pwd = os.getenv('SNOW_PWD')
    body = return_fake_inc_body()
    connection_obj = MakeAsyncSnowConnection(base_url, snow_usr, snow_pwd)
    outcome = asyncio.run(connection_obj.post_single_inc_async(body, how_many=1))
    print("this is the outcome I am looking for: ", outcome[0]['result']['number'])



    # def _get_tasks(self, session, how_many=2):
    #     tasks = []
    #     method = 'GET'
    #     url = f"{self.baseUrl}/api/now/table/incident?sysparm_query=number=INC0010111" 
    #     for _ in range(how_many):
    #         try:
    #             tasks.append(asyncio.create_task(session.request(method, url, auth=aiohttp.BasicAuth(self.username, self.password))))
    #         except Exception as e:
    #             print(e)
    #     return tasks


 

    # async def _make_get_request(self, how_many):
    #     results = []
    #     async with aiohttp.ClientSession() as session: 
    #         tasks = self._get_tasks(session, how_many)
    #         responses = await asyncio.gather(*tasks)
    #         for response in responses:
    #             results.append(await response.json())
    #     return results

    # async def _make_post_request(self, how_many, method, url):
    #     results = []
    #     async with aiohttp.ClientSession() as session: 
    #         tasks = self._post_tasks(session, how_many, method, url)
    #         responses = await asyncio.gather(*tasks)
    #         for response in responses:
    #             results.append(await response.json())
    #     print(results) 

    # def _post_tasks(self, session, how_many, method, url):
    #     tasks = []    
    #     for _ in range(how_many):
    #         tasks.append(asyncio.create_task(session.request(method, url, auth=aiohttp.BasicAuth(self.username, self.password), data=self.payload, headers=self.headers)))
    #     return tasks

    # def _prapare_tasks(self, session, how_many, build_task):
    #     tasks = []
    #     for _ in range(how_many):
    #          tasks.append(asyncio.create_task(build_task))
    #     return tasks


    # async def _get_tasks(self, session, method, url, how_many):
    #     tasks = []
        # method = 'POST'
        # self.payload = {
        #     "impact": 3,
        #     # "description": fake.text(),
        #     "description": 'Mike test',
        # }
        # url = f"{self.baseUrl}/api/now/table/incident" 
        # body = json.dumps(self.payload)
        # for _ in range(how_many):
        #     try:
        #         task = asyncio.ensure_future(asyncio.create_task(session.request(method, url, auth=aiohttp.BasicAuth(self.username, self.password), data=body, headers=self.headers)))
        #         tasks.append(task)
        #     except Exception as e:
        #         print("this is the errror", e)
        # print(tasks)
        # return tasks


    # async def _make_request(self, method, url, how_many):
    #     results = []
    #     async with aiohttp.ClientSession() as session: 
            # build_task = self._prepare_request(session, method, url)
    #         tasks = await self._get_tasks(session, method, url, how_many)
    #         responses = await asyncio.gather(*tasks)
    #         for response in responses: 
    #             results.append(response)
    #         return results
    
  