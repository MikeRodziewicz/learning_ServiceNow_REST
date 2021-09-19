import os 
import requests
from abc import ABC, abstractclassmethod

class Config():

    BASE_URL = os.environ.get('SNOW_BASE_URL') or 'test1'
    USER =  os.environ.get('SNOW_USER') or 'test2'
    PWD = os.environ.get('SNOW_PWD') or 'test3'

    @staticmethod
    def init_app():
        pass


class PDIConfig(Config):
    INCIDENT_SEARCH = 'INC0010111'


# app = PDIConfig()
# print(app.INCIDENT_SEARCH)
# print(app.USER)

class TypeOfRequest(ABC):

    @abstractclassmethod
    def provide_method(self) -> str:
        pass


class GetRequest(TypeOfRequest):

    def provide_method(self):
        return 'get'
    
class PostRequest(TypeOfRequest):

    def provide_method(self):
        return 'post'


spam = GetRequest()
print(spam.provide_method())


# # Set the request parameters
# url = 'https://dev105336.service-now.com/api/now/table/incident?sysparm_query=number%3DINC0010111&sysparm_limit=1'

# # Eg. User name="admin", Password="admin" for this code sample.

# # Set proper headers
# headers = {"Content-Type":"application/json","Accept":"application/json"}

# # Do the HTTP request
# response = getattr(requests, spam.provide_method())(url, auth=(user, pwd), headers=headers )
# # response = requests.get(url, auth=(user, pwd), headers=headers )

# # Check for HTTP codes other than 200
# if response.status_code != 200: 
#     print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
#     exit()

# # Decode the JSON response into a dictionary and use the data
# data = response.json()
# print(data)



# class MakeRequest():

#     # user = os.environ.get('SNOW_USER')
#     # pwd = os.environ.get('SNOW_PWD')
#     # baseUrl = os.environ.get('SNOW_BASE_URL')

#     def __init__(self, http_method: GetRequest, user, pwd, baseUrl):
#         self.http_method = http_method
#         self.user = user
#         self.pwd = pwd
#         self.baseUrl = baseUrl


#     def make_request(self):
#         self.http_method = self.http_method.provide_method()
#         return self.http_method


#     def send_request(self,):
#         response = getattr(requests, 'get')(
#             self.baseUrl + '/api/now/table/incident', auth=(self.user, self.pwd),
#             headers={"Content-Type":"application/json","Accept":"application/json"}, data= {
#                     'sysparm_query': f'number={"INC0010111"}',
#                     'sysparm_limit': '1'
#                 }
#             )
#         data = response.json()
#         print(data)




# app = MakeRequest(GetRequest(), USER, PWD, BASE_URL)
# app.send_request()







