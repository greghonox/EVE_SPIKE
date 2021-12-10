from eve import Eve

from models import cliente, profissao, user, materiais

MONGO_HOST = "localhost"
MONGO_DBNAME = "apitest"
MONGO_AUTH_SOURCE = 'teste'
MONGO_PORT = 27017
# RECONHECE OS .py MODELOS AUTOMATICAMENTE
settings = {
    "DOMAIN": {
        "usuario": user.shema,
        "cliente": cliente.schema,
        "material": materiais.shema,
        "profissao": profissao.schema,
    }
}

app = Eve(settings=settings)
app.run(debug=True)
