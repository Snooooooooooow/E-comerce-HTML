from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Produto, SiteConfig


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ("logo", "updated_at")
    readonly_fields = ("updated_at",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "preco", "promocao", "data_criacao")
    list_filter = ("categoria", "promocao")
    search_fields = ("nome", "descricao")
    fields = ("nome", "descricao", "preco", "promocao", "imagem", "categoria", "trailer", "data_criacao")
    readonly_fields = ("data_criacao",)


    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="max-height: 50px;" />', obj.imagem.url)
        return "-"
    imagem_preview.short_description = "Preview"















