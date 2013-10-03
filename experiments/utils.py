import random
import string


def generate_things(num_things):
    """
    Generate a list of dictionaries with length `num_things`. Each item will
    be of the format:

        {
            "name": "some string",
            "number": <integer
        }
    """
    things = []
    for x in range(num_things):
        thing = {
            'name': generate_random_string(),
            'number': random.randint(10000, 100000)
        }
        things.append(thing)
    return things


def generate_random_string(length=8):
    """
    Generate a random string of length `length` using ascii uppercase chars.
    """
    return ''.join(random.choice(string.ascii_uppercase) for x in range(length))
