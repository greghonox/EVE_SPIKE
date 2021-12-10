shema = {
    "resource_methods": ["POST", "GET", "DELETE"],
    "item_methods": ["PUT", "PATCH", "GET"],
    "query_objectid_as_string": True,
    "schema": {
        "nome": {
            "type": "string",
        },
        "qtde": {
            "type": "integer"
        },
        "tamanho": {
            "type": "integer"
        },
        "cor": {
            "type": "string"
        },
    }
}
