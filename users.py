import db
from connexion import request

USERS = {
    "1": {
        "id": "1",
        "name": "Tom"
    },
    "2": {
        "id": "2",
        "name": "John"
    },
    "3": {
        "id": "3",
        "name": "Simon"
    }
}


def read():
    # return [USERS[key] for key in sorted(USERS.keys())]
    return db.read_users()

