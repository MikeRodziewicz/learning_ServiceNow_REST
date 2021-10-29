from faker import Faker
import random

fake = Faker()


def return_fake_inc_body() -> dict:
    body = {
        "impact": random.randint(1,5),
        # "description": fake.text(),
        "description": 'Mike test',
    }
    return body


if __name__ == "__main__":
    pass