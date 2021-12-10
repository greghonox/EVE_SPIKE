from json import loads


def pre_cliente(request):
    print(f"PROCESSANDO {loads(request.data)}")
    return loads(request.data)
