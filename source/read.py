import json
from collections import namedtuple
from pprint import pprint

def read_json_to_object(filename):
    with open(filename, "r") as f:
        data = f.read()

    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    print(x.name)
    print([x.name for x in x.friends.data])

def main():
    """
    Given a file, return an object
    :return: None
    """
    filename = 'users.json'
    read_json_to_object(filename)

if __name__ == "__main__":
    main()