import requests
import os
import asyncio
import aiohttp
from dotenv import load_dotenv
from utils import return_fake_inc_body
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
    
    async def get_incidents_async(self, incidents_list:list):
        method = "GET"
        results = []
        urls = []
        for inc in incidents_list:
            url = f"{self.baseUrl}/api/now/table/incident?sysparm_query=number={inc}"
            urls.append(url)
        async with aiohttp.ClientSession(headers=self.headers, auth=aiohttp.BasicAuth(self.username, self.password)) as session:
            tasks = [session.request(url=url, method=method) for url in urls]
            responses = await asyncio.ensure_future(asyncio.gather(*tasks, return_exceptions=True))
            for response in responses:
                results.append(await response.json())
            return results

    async def post_multiple_incidents_async(self, body:list):
        url = f"{self.baseUrl}/api/now/table/incident"
        method = "POST"
        results = []
        async with aiohttp.ClientSession(headers=self.headers, auth=aiohttp.BasicAuth(self.username, self.password)) as session:
            tasks = [session.request(url=url, method=method, json=item)for item in body]
            responses = await asyncio.ensure_future(asyncio.gather(*tasks, return_exceptions=True))
            print("this is the response i want",len(responses))
            for response in responses:
                print(response)
                results.append(await response.json())
            return results


if __name__ == "__main__":
    pass
  