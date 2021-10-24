
import requests


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
            self.response = self.response.json()
            return self.response
        except requests.exceptions.HTTPError as errh:
            print(errh)

    def get_single_incident(self, inc_number: str):
        method = "GET"
        url = f"{self.baseUrl}/api/now/table/incident?sysparm_query=number={inc_number}"
        return self._make_connection(method, url)

    def post_single_incident(self, body: dict):
        method = "POST"
        self.payload = body
        url = f"{self.baseUrl}/api/now/table/incident"
        return self._make_connection(method, url)

    def get_all_emails(self, data):
        method = "GET"
        url = f"{self.baseUrl}/api/now/table/sys_email?sysparm_limit={data['sysparm_limit']}&sysparm_query={data['sysparm_query']}"
        return self._make_connection(method, url)
        
    def get_single_email(self, sys_id:str):
        method = "GET"
        url = f"{self.baseUrl}/api/now/v1/email/{sys_id}"
        return self._make_connection(method, url)


if __name__ == "__main__":
    pass
   
