from django import forms
from .models import Produto, ImagemProduto

class ProdutoDescricaoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao']

class ImagemProdutoForm(forms.ModelForm):
    class Meta:
        model = ImagemProduto
        fields = ['imagem', 'descricao']
