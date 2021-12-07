shema = {
    "resource_methods": ["POST", "GET"],
    "schema": {
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "username": {"type": "string", "unique": True},
        "phone": {"type": "string"},
    },
}
