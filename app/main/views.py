from django.shortcuts import render
from app.init.models import Todo, User, Image
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from app.init.forms import TodoForm, ImageForm
from app.main.utils import (
    get_time_diff_days,
    get_label,
    clean_dict,
    adjust_boolean_fields,
)

@login_required
def anotacoes(request, id_user):
    if request.user.id != id_user:
        return redirect('main:login')

    filters = {
        "tag": request.GET.get('tag', None),
        "prioridade": get_label(request.GET.get('prioridade', "")),
        "favorito": request.GET.get('favorito', ""),
        "completo": request.GET.get('completo', ""),
        "titulo": request.GET.get('titulo', ""),
        "user": get_object_or_404(User,id=id_user),
        "is_active": True,
    }

    todos = Todo.objects.filter(
         **adjust_boolean_fields(
                clean_dict(filters)
            )
    )

    print(f"Todas: ", [item.prazo_dias for item in todos])
    context = {
        "anotacoes": todos,
        "all_tags": Todo.TAGS, # Envia todas as tags para o template
        "all_prioridades": Todo.PRIORIDADES, # Envia todas as prioridades para o template
        "selected_tag": filters.get('tag'), # Envia o filtro aplicado para o template
        "selected_prioridade": filters.get('prioridade'),
        "selected_favorito": filters.get('favorito'),
        "selected_completo": filters.get('completo'),
        "selected_titulo": filters.get('titulo'),
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
