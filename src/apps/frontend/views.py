from django.shortcuts import (
    render,
    redirect
)

from django.contrib.auth.decorators import login_required


def serve_protected_file(file_name):
    @login_required
    def view(request):
        return render(
            request=request,
            template_name=file_name
        )
    
    return view


def serve_file(file_name, login_required=False):
    pass


def home(request):
    return render(
        request=request,
        template_name="landing_page.html"
    )

def password_reset(request):
    return render(
        request=request,
        template_name="registration/password_reset.html"
    )

def visu_publica(request):
    return render(
        request=request,
        template_name="visu_publica.html"
    )

def lista_pontos(request):
    return render(
        request=request,
        template_name="lista_pontos.html"
    )

@login_required
def sequencia_coletas(request):
    return render(
        request=request,
        template_name="privado/sequencia_coletas.html"
    )

@login_required
def pontos_coletas(request):
    return render(
        request=request,
        template_name="privado/pontos_coletas.html",
        # context=context
    )

@login_required
def criar_ponto(request):
    # if request.method == 'POST':
    #     form = FormPontoColeta(request.POST)
    #     form.save()
    # form = FormPontoColeta()

    return render(
        request=request,
        template_name="privado/criar_ponto.html",
        # context={ 'form': form }
    )


@login_required
def editar_ponto(request, ponto_id: int):
    # ponto = get_object_or_404(
    #     PontoColeta,
    #     id=ponto_id
    # )

    # if request.method == 'POST':
    #     form = FormPontoColeta(request.POST, instance=ponto)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(pontos_coletas)
    # else:
    #     form = FormPontoColeta(instance=ponto)

    return render(
        request,
        'privado/editar_ponto.html',
        # {'form': form}
    )


@login_required
def ponto_coleta(request, ponto_id: int):
    # ponto = get_object_or_404(
    #     PontoColeta,
    #     id=ponto_id
    # )

    # context = {
    #     "ponto": ponto
    # }

    return render(
        request=request,
        template_name="privado/ponto_coleta.html",
        # context=context
    )


@login_required
def ponto_coleta_relatorio(request, ponto_id: int, amostragem: int):
    # ponto = get_object_or_404(
    #     PontoColeta,
    #     id=ponto_id
    # )

    # context = {
    #     "pontos": get_hierarquia(ponto, amostragem),
    #     "amostragem": amostragem,
    # }

    return render(
        request=request,
        template_name="privado/ponto_coleta_relatorio.html",
        # context=context
    )


@login_required
def criar_coleta(request):
    # ponto_id = request.GET.get('p')
    # amostragem = request.GET.get('amostragem')
    # ponto = PontoColeta.objects.get(id = int(ponto_id))

    # if request.method == 'POST':
    #     form = FormColeta(request.POST)
    #     form.save()

    #     next_url = request.GET.get('next')
    #     if next_url:
    #         return HttpResponseRedirect(next_url)
    
    # pontos = get_hierarquia(ponto, amostragem)

    # form = FormColeta(initial={
    #     'amostragem': amostragem
    # })
    
    # if pontos:
    #     choices = [(p['id'], p['nome']) for p in pontos]
    #     form.fields['ponto_coleta'] = ChoiceField(choices=choices)
    
    return render(
        request=request,
        template_name='privado/criar_coleta.html',
        # context={ 'form': form }
    )


@login_required
def criar_amostragem(request, ponto_id: int):
    # ponto = get_object_or_404(
    #     PontoColeta,
    #     id=ponto_id
    # )
    # amostragem, created = Amostragem.objects.get_or_create(
    #     amostragem=ponto.amostragens.count() + 1
    # )
    # ponto.amostragens.add(amostragem)
    return redirect(
        ponto_coleta,
        # ponto_id=ponto_id
    )


@login_required
def editar_coleta(request, coleta_id: int):
    # coleta = Coleta.objects.get(id=coleta_id)
    # form = FormColeta(instance=coleta)

    # if request.method == 'POST':
    #     form = FormColeta(request.POST, instance=coleta)
    #     form.save()

    #     next_url = request.GET.get('next')
    #     if next_url:
    #         return HttpResponseRedirect(next_url)
    
    return render(
        request=request,
        template_name='privado/editar_coleta.html',
        # context={ 'form': form }
    )


@login_required
def configuracoes(request):
    # context = {
    #     'users': User.objects.all()
    # }
    return render(
        request=request,
        template_name="privado/configuracoes.html",
        # context=context
    )


@login_required
def edificacoes(request):
    # search = request.GET.get("q")
    # if search:
    #     edificacoes = Edificacao.objects.filter(
    #         Q(nome__contains=search) | Q(codigo__contains=search)
    #     )
    # else:
    #     edificacoes = Edificacao.objects.all()

    # context = {
    #     'edificacoes': edificacoes
    # }

    return render(
        request=request,
        template_name='privado/edificacoes.html',
        # context=context
    )


@login_required
def criar_edificacao(request):
    # if request.method == 'POST':
    #     form = FormEdificacao(request.POST)
    #     form.save()
    # form = FormEdificacao()

    return render(
        request=request,
        template_name='privado/criar_edificacao.html',
        # context={ 'form': form}
    )


@login_required
def excluir_edificacao(request, edificacao_id: int):
    pass


@login_required
def edificacao(request, cod_edificacao: str):
    
    return render(
        request=request,
        template_name='privado/editar_edificacao.html'
    )

@login_required
def excluir_usuario(request, id:int):
    # if request.POST:
    #     User.objects.filter(pk=id).delete()
    return redirect(configuracoes)