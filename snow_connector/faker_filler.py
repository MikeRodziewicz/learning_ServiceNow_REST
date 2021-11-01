from faker import Faker
import random
import json

fake = Faker()


def return_fake_inc_body(how_many:int) -> dict:
    body_dumps = []
    for _ in range(how_many): 
        body = {
            "impact": random.randint(1,5),
            # "description": fake.text(),
            "description": 'Mike test',
        }
        body_dumps.append(body)
    return json.dumps(body_dumps)

if __name__ == "__main__":
     test = return_fake_inc_body(2)
     print(type(test))
     print(test)
    #  for i in test:
    #      print(test(i))