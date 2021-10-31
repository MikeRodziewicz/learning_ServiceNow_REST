import requests
import asyncio
import aiohttp

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

    # def _get_tasks(self, session, how_many):
    #     tasks = []
    #     method = 'GET'
    #     url = f"{self.baseUrl}/api/now/table/incident?sysparm_query=number=INC0010111" 
    #     for _ in how_many:
    #         tasks.append(asyncio.create_task(session.request(method, url, auth=aiohttp.BasicAuth(self.username, self.password))))
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

    def _prapare_tasks(self, session, how_many, build_task):
        tasks = []
        for _ in range(how_many):
             tasks.append(asyncio.create_task(build_task))
        return tasks

    async def _prepare_request(self, session, method, url):
        try:
            async with session.request(method, url, auth=aiohttp.BasicAuth(self.username, self.password), data=self.payload, headers=self.headers) as response:
                print(response)
                # if response == 200:
                #     print("Status:", response.status)
                #     print("Content-type:", response.headers['content-type'])
                #     html = await response.text()
                #     print("Body:", html)
        except aiohttp.ClientHttpProxyError as e:
            print('Connector Error', str(e))

    async def _make_request(self, how_many, method, url):
        results = []
        async with aiohttp.ClientSession() as session: 
            print(session)
            build_task = self._prepare_request(session, method, url)
            print(build_task)
            tasks = self._prapare_tasks(session, how_many, build_task)
            print(tasks)
            responses = await asyncio.gather(*tasks)
            print(responses)
            for response in responses: 
                results.append(await response)
            return results
    
    async def post_single_inc_async(self, body:dict, how_many):
        method = "POST"
        print(body)
        self.payload = body
        print(self.payload)
        url = f"{self.baseUrl}/api/now/table/incident"
        await self._make_request(how_many, method, url)

if __name__ == "__main__":
    pass
   
