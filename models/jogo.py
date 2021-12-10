schema = {
    "resource_methods": ["POST", "GET", "DELETE"],
    "item_methods": ["PUT", "PATCH", "GET"],
    "query_objectid_as_string": True,
    "schema":
        {
        "game_id": {
            "type": "string",
            "required": True,
        },
        "titulo": {
            "type": "string",
            "required": False,
        },
            "nome": {
            "type": "string",
            "required": False,
        },
    }
}
