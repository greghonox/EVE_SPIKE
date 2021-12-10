from eve import Eve

from models import cliente, profissao, user, materiais, jogo, imagem, pessoa

MONGO_HOST = "localhost"
MONGO_DBNAME = "apitest"
MONGO_AUTH_SOURCE = 'teste'
MONGO_PORT = 27017
# FUNCIONA DE FORMA GLOBAL MAS RESPEITA O QUE ESTIVER NO SCHEMA
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
# FUNCIONA DE FORMA GLOBAL MAS RESPEITA O QUE ESTIVER NO SCHEMA
ITEM_METHODS = ['GET', 'PUT', 'PATCH', 'DELETE']

settings = {
    "DOMAIN": {
        "jogo": jogo.schema,
        "usuario": user.schema,
        "imagem": imagem.schema,
        "pessoa": pessoa.schema,
        "cliente": cliente.schema,
        "material": materiais.schema,
        "profissao": profissao.schema,
    }
}

app = Eve(settings=settings)
app.run(debug=True)
