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

    def _get_tasks(self, session, urls, method):
        tasks = []
        for url in urls:
                tasks.append(asyncio.create_task(session.request(url=url, method=method, auth=aiohttp.BasicAuth(self.username, self.password), data=self.payload, headers=self.headers)))
        return tasks

    async def _make_connection(self, method, urls):
        outcome = []
        async with aiohttp.ClientSession() as session:
            tasks = self._get_tasks(session, urls, method)
            responses = await asyncio.ensure_future(asyncio.gather(*tasks, return_exceptions=True))
            for response in responses:
                outcome.append(await response.json())
            return outcome

    async def post_single_inc_async(self, body:dict, how_many):
        method = "POST"
        self.payload = json.dumps(body)
        url = f"{self.baseUrl}/api/now/table/incident"
        outcome = await self._make_connection(method, url, how_many)
        return outcome


    async def get_single_inc_async(self, inc_number):
        how_many = len(inc_number)
        method = "GET"
        urls = []
        for inc in inc_number:
            url = f"{self.baseUrl}/api/now/table/incident?sysparm_query=number={inc}"
            urls.append(url)
        outcome = await self._make_connection(method, urls)
        return outcome

if __name__ == "__main__":
    load_dotenv()
    base_url = os.getenv('BASE_URL')
    snow_usr = os.getenv('SNOW_USR')
    snow_pwd = os.getenv('SNOW_PWD')
    body = return_fake_inc_body()
    inc_numbers = ['INC0010058','INC0010057','INC0010059','INC0010060']
    connection_obj = MakeAsyncSnowConnection(base_url, snow_usr, snow_pwd)
    # outcome = asyncio.run(connection_obj.post_single_inc_async(body, how_many=1))
    outcome = asyncio.run(connection_obj.get_single_inc_async(inc_numbers))
    # print("this is the outcome I am looking for: ", outcome[0]['result']['number'])
    print(outcome)
    

  