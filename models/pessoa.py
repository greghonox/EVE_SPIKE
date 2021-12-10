schema = {
    "resource_methods": ["POST", "GET"],
    "item_methods": ["PUT", "PATCH", "GET", "DELETE"],
    "query_objectid_as_string": True,
    "url": "cliente/<regex('[a-z0-9]{24}'):cliente_id>/pessoa",
    "schema": {
        "idade": {
            "type": "integer",
            "required": False
        },
        "cor": {
            "type": "string",
            "required": False
        },
        "cliente_id": {
            'type': 'objectid',
            'required': False,
            'data_relation': {
                    'resource': 'cliente',
                    'field': '_id'
            }
        }
    },

}
