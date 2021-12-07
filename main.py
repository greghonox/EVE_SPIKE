from eve import Eve

from models import cliente, profissao, user

MONGO_HOST = "localhost"
MONGO_DBNAME = "apitest"
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
