schema = {
    "resource_methods": ["POST", "GET"],
    "schema": {
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "username": {"type": "string", "unique": True},
        "password": {"type": "string"},
        "phone": {"type": "string"},
    },
}
