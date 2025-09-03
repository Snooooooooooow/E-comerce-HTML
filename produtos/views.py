from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoDescricaoForm, ImagemProdutoForm

def produto_detalhe(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    imagens = produto.imagens.all()

    if request.method == 'POST':
        desc_form = ProdutoDescricaoForm(request.POST, instance=produto)
        img_form = ImagemProdutoForm(request.POST, request.FILES)

        if 'update_desc' in request.POST and desc_form.is_valid():
            desc_form.save()
            return redirect('produto_detalhe', produto_id=produto.id)

        if 'upload_image' in request.POST and img_form.is_valid():
            nova_imagem = img_form.save(commit=False)
            nova_imagem.produto = produto
            nova_imagem.save()
            return redirect('produto_detalhe', produto_id=produto.id)
    else:
        desc_form = ProdutoDescricaoForm(instance=produto)
        img_form = ImagemProdutoForm()

    context = {
        'produto': produto,
        'imagens': imagens,
        'desc_form': desc_form,
        'img_form': img_form
    }
    return render(request, 'produtos/produto_detalhe.html', context)
