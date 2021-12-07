from eve import Eve

from models import cliente, profissao, user

RESOURCE_METHODS = ["GET", "POST"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]
MONGO_HOST = "localhost"
MONGO_PORT = 27017
# RECONHECE OS .py MODELOS AUTOMATICAMENTE
settings = {
    "DOMAIN": {
        "cliente": cliente.schema,
        "profissao": profissao.schema,
        "usuario": user.shema,
    }
}

app = Eve(settings=settings)
app.run(debug=True)
