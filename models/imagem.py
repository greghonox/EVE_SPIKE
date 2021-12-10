schema = {
    "resource_methods": ["POST", "GET"],
    "item_methods": ["PUT", "PATCH", "GET", "DELETE"],
    "query_objectid_as_string": True,
    "url": "jogo/<regex('[a-z0-9]{24}'):game_id>/imagem",
    "schema":
        {
            "caminho": {
                "type": "string"
            },
            "game_id": {
                'type': 'objectid',
                'required': False,
                'data_relation': {
                    'resource': 'jogo',
                    'field': '_id'
                }
            }
    },
}
