import os
import requests
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
            self.response = requests.request(method=method, url=url, headers=self.headers, data=self.payload, **kwargs)
            self.response.raise_for_status()
            self.response = self.response.json()
            return self.response
        except requests.exceptions.HTTPError as errh:
            print(errh)

    def get_single_incident(self, inc_number):
        method = "GET"
        sysparm_query = f"sysparm_query=number={inc_number}"
        url = f"{self.baseUrl}/api/now/table/incident/{sysparm_query}"
        print(url)
        return self._make_connection(method, url)


base_url = os.getenv('BASE_URL')
snow_usr = os.getenv('SNOW_USR')
snow_pwd = os.getenv('SNOW_PWD')

spam = MakeSnowConnection(base_url, snow_usr, snow_pwd)
print(spam.get_single_incident('INC0000060'))



