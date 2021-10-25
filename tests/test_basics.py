import os
import unittest
from snow_connector import MakeSnowConnection
from dotenv import load_dotenv

class BasicTestCase(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        self.base_url = os.getenv('BASE_URL')
        self.snow_usr = os.getenv('SNOW_USR')
        self.snow_pwd = os.getenv('SNOW_PWD')
        self.connection = MakeSnowConnection(self.base_url, self.snow_usr, self.snow_pwd)


    def test_get_variable_url(self):
        self.base_url = os.getenv('BASE_URL')
        self.assertTrue(self.base_url != None)
    
    def test_get_variable_user(self):
        self.base_url = os.getenv('SNOW_USR')
        self.assertTrue(self.base_url != None)

    def test_get_variable_password(self):
        self.base_url = os.getenv('SNOW_PWD')
        self.assertTrue(self.base_url != None)

    def test_get_single_inc(self):
        response = self.connection.get_single_incident("INC0010111")
        self.assertEqual(response.status_code, 200)
        

