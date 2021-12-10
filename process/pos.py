from json import loads


def pos_cliente(request, payload):
    print(f"PROCESSANDO {loads(request.data)}")
    return loads(request.data)
