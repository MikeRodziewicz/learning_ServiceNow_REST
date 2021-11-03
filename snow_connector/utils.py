from datetime import datetime, timedelta
from faker import Faker
import random
import json


fake = Faker()


def current_time():
    return datetime.now()

def time_for_query(frequency:int):
    now = datetime.now()
    return now - timedelta(seconds=frequency)

def return_fake_inc_body(how_many:int) -> dict:
    """returns a fake body to be used for Incident record"""
    body_dumps = []
    for _ in range(how_many): 
        body = {
            "impact": random.randint(1,5),
            "description": fake.text(),
            "short_description": 'Mike test',
            }
        body_dumps.append(body)
    return json.dumps(body_dumps)


if __name__ == "__main__":
    pass