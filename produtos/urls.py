from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('produtos/<int:produto_id>/', views.produto_detalhe, name='produto_detalhe'),
]
