from eve import Eve

from models import cliente, profissao, user, materiais, jogo, imagem

MONGO_HOST = "localhost"
MONGO_DBNAME = "apitest"
MONGO_AUTH_SOURCE = 'teste'
MONGO_PORT = 27017
# RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
# ITEM_METHODS = ['GET', 'PUT', 'PATCH', 'DELETE']

settings = {
    "DOMAIN": {
        "jogo": jogo.schema,
        "usuario": user.schema,
        "imagem": imagem.schema,
        "cliente": cliente.schema,
        "material": materiais.schema,
        "profissao": profissao.schema,
    }
}

app = Eve(settings=settings)
app.run(debug=True)
