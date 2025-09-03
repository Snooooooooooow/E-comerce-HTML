from django.http import HttpResponse

def lista_clientes(request):
    return HttpResponse("lista de clientes")