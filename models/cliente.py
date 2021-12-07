schema = {
    "resource_methods": ["POST", "GET"],
    "item_methods": ["PUT", "PATCH", "GET"],
    "query_objectid_as_string": True,
    "schema": {
        "external_id": {"type": "string", "required": True, "unique": True},
        "insured_data": {
            "type": "objectid",
            "required": False,
            "data_relation": {
                "resource": "insured_data",
                "field": "_id",
                "embeddable": True,
            },
        },
        "broker_data": {
            "type": "objectid",
            "required": False,
            "data_relation": {
                "resource": "broker_data",
                "field": "_id",
                "embeddable": True,
            },
        },
    },
}
