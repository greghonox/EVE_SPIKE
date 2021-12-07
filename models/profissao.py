schema = {
    "pagination": False,
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH"],
    "public_methods": ["GET"],
    "public_item_methods": ["GET", "PATCH"],
    "schema": {
        "name": {"type": "string", "required": True, "unique": True},
        "cbo_code": {"type": "string", "required": True, "nullable": True},
        "subgroup_code": {"type": "string", "required": False, "nullable": True},
        "requires_description": {
            "type": "boolean",
            "required": False,
            "default": False,
        },
        "coverages": {
            "type": "list",
            "required": False,
            "schema": {
                "type": "dict",
                "schema": {
                    "coverage_id": {"type": "string", "required": True},
                    "max_covered_capital": {
                        "type": "number",
                        "min": 0,
                        "required": True,
                        "nullable": True,
                    },
                    "pricing_factor": {
                        "type": "number",
                        "min": 0,
                        "required": True,
                    },
                },
            },
        },
    },
}
