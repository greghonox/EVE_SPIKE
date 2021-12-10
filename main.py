from eve import Eve

from models import cliente, profissao, user, material, jogo, imagem, conta, pessoa
from process.pre import pre_cliente
from process.pos import pos_cliente

MONGO_HOST = "localhost"
MONGO_DBNAME = "teste"
MONGO_AUTH_SOURCE = 'teste'
MONGO_PORT = 27017
# FUNCIONA DE FORMA GLOBAL MAS RESPEITA O QUE ESTIVER NO SCHEMA
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
# FUNCIONA DE FORMA GLOBAL MAS RESPEITA O QUE ESTIVER NO SCHEMA
ITEM_METHODS = ['GET', 'PUT', 'PATCH', 'DELETE']

settings = {
    "DOMAIN": {
        "jogo": jogo.schema,
        "conta": conta.schema,
        "usuario": user.schema,
        "imagem": imagem.schema,
        "pessoa": pessoa.schema,
        "cliente": cliente.schema,
        "material": material.schema,
        "profissao": profissao.schema,
    }
}

app = Eve(settings=settings)

app.on_pre_POST_cliente += pre_cliente
app.on_post_POST_cliente += pos_cliente

app.run(debug=True)
