from django.shortcuts import render
from app.init.models import Todo, User, Image
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from app.init.forms import TodoForm, ImageForm
from . import utils

@login_required
def anotacoes(request, id_user):
    if request.user.id != id_user:
        return redirect('main:login')

    # Começamos com todos os objetos Todo para o usuário
    todos = Todo.objects.filter(user=get_object_or_404(User, id=id_user), is_active=True)

    # Aplicar filtros com base nos query parameters
    tag_filter = request.GET.get('tag')
    prioridade_filter = request.GET.get('prioridade')
    favorito_filter = request.GET.get('favorito')
    completo_filter = request.GET.get('completo')
    titulo_filter = request.GET.get('titulo')

    if tag_filter:
        todos = todos.filter(tag=tag_filter, is_active=True)
    if prioridade_filter:
        todos = todos.filter(prioridade=prioridade_filter, is_active=True)
    if favorito_filter:
        # 'true' ou 'false' vindo da URL. Convertemos para booleano
        todos = todos.filter(favorito=(favorito_filter.lower() == 'true'), is_active=True)
    if completo_filter:
        todos = todos.filter(completo=(completo_filter.lower() == 'true'), is_active=True)
    if titulo_filter: # <--- NOVO: Aplica o filtro de título
        # Usamos icontains para busca case-insensitive e parcial
        todos = todos.filter(titulo__icontains=titulo_filter, is_active=True)
    prazos = {} # Parece que 'prazos' não está sendo usado, mas mantive por consistência

    for tarefa in todos:
        # Atribuição de dias restantes
        if tarefa.prazo_inicial and tarefa.prazo_final:
            tarefa.prazo = utils.get_time_diff_days(tarefa.prazo_inicial, tarefa.prazo_final)
        else:
            tarefa.prazo = "Sem prazo definido"

        # Mensagens
        try:
            if int(tarefa.prazo) < 0:
                tarefa.message = "Passou do prazo: "
            else:
                tarefa.message = "Dias restantes: "
        except ValueError: # Caso tarefa.prazo seja "Sem prazo definido"
            tarefa.message = ""

        # Cores das mensagens
        try:
            if int(tarefa.prazo) >= 7:
                tarefa.color = "green"
            elif 3 <= int(tarefa.prazo) < 7:
                tarefa.color = "orange"
            elif 1 <= int(tarefa.prazo) <= 2:
                tarefa.color = "red"
            else:
                tarefa.color = "violet"
        except ValueError:
            tarefa.color = "gray" # Cor padrão para "Sem prazo definido"

    context = {
        "anotacoes": todos,
        "prazos": prazos,
        "all_tags": Todo.TAGS, # Envia todas as tags para o template
        "all_prioridades": Todo.PRIORIDADES, # Envia todas as prioridades para o template
        "selected_tag": tag_filter, # Envia o filtro aplicado para o template
        "selected_prioridade": prioridade_filter,
        "selected_favorito": favorito_filter,
        "selected_completo": completo_filter,
        "selected_titulo": titulo_filter,
    }

    return render(request, "anotacoes.html", context)


@login_required()
def show(request, id_user,id_anotacao):
    form = ImageForm()

    if request.user.id != id_user:
        return redirect("main:login")
    task = get_object_or_404(Todo, id=id_anotacao)
    user = get_object_or_404(User, id=id_user)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            # Atribuindo a imagem a anotação correta
            image.user = get_object_or_404(Todo, id=id_anotacao)
            image.save()
        else:
            print("Errors:", form.errors)

    imgs = Image.objects.filter(user=get_object_or_404(Todo, id=id_anotacao))
    context = {
        "tarefa":task,
        "user": user,
        "form":form,
        "imagens": imgs,
    }
    return render(request, "show.html", context)


@login_required()
def editar(request, id_user, id_anotacao):
    todo = get_object_or_404(Todo, id=id_anotacao)
    user = get_object_or_404(User, id=id_user)
    form = TodoForm(instance=todo)

    #Consertar com o login_required
    if request.user.id != id_user:
        return redirect('main:login')

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        todo = form.save(commit=False)
        todo.user = user
        todo.save()
        return redirect("main:anotacoes", id_user=id_user)
    else:
        print(form.errors)

    context = {
        "user":user,
        "form":form,
        "tarefa":todo

    }
    return render (request, "editar.html", context)


@login_required()
def remover(request, id_user, id_anotacao):
    #Consertar com o login_required
    if request.user.id != id_user:
        return redirect('main:login')

    todo = get_object_or_404(Todo, id=id_anotacao)
    user = get_object_or_404(User, id=id_user)
    form = TodoForm(instance=todo)

    if request.method == "POST":
        todo.is_active = False
        todo.save()
        return redirect("main:anotacoes", id_user=id_user)
    else:
        print("Erros no formulario: ", form.errors)
        return render (request, "delete.html", {"user":user, "tarefa":todo})


@login_required()
def apagar_imagem(request, id_user, id_imagem,id_anotacao):
    image = get_object_or_404(Image, id=id_imagem)
    user = get_object_or_404(User, id=id_user)
    todo = get_object_or_404(Todo, id=id_anotacao)

    form = ImageForm(instance=image)

    #Consertar com o login_required
    if request.user.id != id_user:
        return redirect('main:login')

    if request.method == "POST":
        image.delete()
        return redirect("main:show", id_user=id_user, id_anotacao=id_anotacao)
    else:
        print(form.errors)
    return render (request, "apagar_imagem.html", {"user":user, "imagem":image, "tarefa":todo})


@login_required()
def editar_descricao(request, id_user, id_imagem, id_anotacao):
    image = get_object_or_404(Image, id=id_imagem)
    user = get_object_or_404(User, id=id_user)
    todo = get_object_or_404(Todo, id=id_anotacao)
    form = ImageForm(request.POST, request.FILES, instance=image)

    #Consertar com o login_required
    if request.user.id != id_user:
        return redirect('main:login')

    if request.method == "POST":
        image = form.save(commit=False)
        image.user = todo
        image.save()

        return redirect("main:show", id_user=id_user, id_anotacao=id_anotacao)
    else:
        print(form.errors)

    context = {
        "user":user,
        "imagem":image,
        "tarefa":todo,
        "form":form
    }
    return render (request, "editar_descricao.html", context)

def not_found(request):
    return render(request, "404.html")
