import json
from json.decoder import JSONDecodeError
def load_users():
    try:
        with open("users.txt", "r") as file:
            contents = file.read()

        return json.load(contents)
    except FileNotFoundError:
        return {}
    except JSONDecodeError:
        return {}