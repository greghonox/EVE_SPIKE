from eve import Eve

settings = {
    "DOMAIN": {
        "minha_seguradora": {
            "coverages": {
                "type": "list",
                "required": False,
                "schema": {
                    "type": "dict",
                    "schema": {
                        "code": {
                            "type": "string",
                            "required": True,
                        },
                        "coverage_chosen": {
                            "type": "integer",
                            "min": 0,
                            "required": True,
                        },
                    },
                },
            },
            "status": {
                "type": "string",
                "required": False,
                "default": "open",
                "allowed": ["open", "closed", "filed"],
            },
        }
    }
}

app = Eve(settings=settings)
app.run(debug=True)
