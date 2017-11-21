import json
from collections import namedtuple
from pprint import pprint

def read_json_to_object(filename):
    with open(filename, "r") as f:
        data = f.read()

    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    x, i = filter_people_with_no_firends(x)
    print(x)
    print(i)

def filter_people_with_no_firends(x):
    """
    res is all friends of the original person
    i is the number of friends that need to requery because they don't have friends
    """
    res = []
    i = 0
    for friend in x.friends.data:
        try:
            if len(friend.friends.data) > 0:
                res.append(friend)
        except Exception as e:
            i += 1
            pass
        else:
            pass
    return res, i

def is_self(friend, id):
    return friend.id == id

def main():
    """
    Given a file, return an object
    :return: None
    """
    filename = 'users.json'
    read_json_to_object(filename)

if __name__ == "__main__":
    main()