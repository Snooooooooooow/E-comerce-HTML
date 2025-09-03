from django.http import HttpResponse

def lista_pedidos(request):
    return HttpResponse("lista de pedidos")