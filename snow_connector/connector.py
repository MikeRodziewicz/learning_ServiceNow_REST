import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()


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
            self.response.raise_for_status()
            self.response = self.response.json()
            return self.response
        except requests.exceptions.HTTPError as errh:
            print(errh)

    def get_single_incident(self, inc_number):
        method = "GET"
        url = f"{self.baseUrl}/api/now/table/incident?sysparm_query=number={inc_number}"
        return self._make_connection(method, url)

    def post_single_incident(self, body):
        method = "POST"
        self.payload = body
        url = f"{self.baseUrl}/api/now/table/incident"
        return self._make_connection(method, url)


if __name__ == "__main__":
    
    base_url = os.getenv('BASE_URL')
    snow_usr = os.getenv('SNOW_USR')
    snow_pwd = os.getenv('SNOW_PWD')
    body = {
        "urgency": "1",
        "impact": "3",
        "short_description": "test description"
        }

    spam = MakeSnowConnection(base_url, snow_usr, snow_pwd)

    print(spam.post_single_incident(body))
