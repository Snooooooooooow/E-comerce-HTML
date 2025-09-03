from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    promocao = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    trailer = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="ID do YouTube (exemplo: dQw4w9WgXcQ)"
    )

    def __str__(self):
        return self.nome

class SiteConfig(models.Model):
    logo = models.ImageField(upload_to='logos/', null=True, blank=True, verbose_name='Logo do Site')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Configuração do Site"

class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/galeria/')
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"Imagem de {self.produto.nome}"
