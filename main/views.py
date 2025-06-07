from django.shortcuts import render
from init.models import Todo, User, Image
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from init.forms import TodoForm, ImageForm
from . import utils

@login_required
def anotacoes(request, id_user):
    if request.user.id != id_user:
        return redirect('login')

    todos = Todo.objects.all()
    prazos = {}

    for tarefa in todos:

        #Atribuição de dias restantes
        if tarefa.prazo_inicial and tarefa.prazo_final:
            tarefa.prazo = utils.get_time_diff_days(tarefa.prazo_inicial, tarefa.prazo_final)
        else:
            tarefa.prazo = "Sem prazo definido"

        #Mensagens
        if int(tarefa.prazo) <=0:
            tarefa.message = "Passou do prazo: "
        else:
            tarefa.message = "Dias restantes: "

        #Cores das menssagens
        if int(tarefa.prazo) >= 7:
            tarefa.color = "green"
        elif int(tarefa.prazo) >= 3 and int(tarefa.prazo) < 7:
            tarefa.color = "orange"
        elif int(tarefa.prazo) >= 1 and int(tarefa.prazo) <=2:
            tarefa.color = "red"
        else:
            tarefa.color = "violet"

    context = {
        "anotacoes":todos,
        "prazos":prazos,
    }

    return render(request, "anotacoes.html", context)


def show(request, id_user,id_anotacao):
    form = ImageForm()

    if request.user.id != id_user:
        return redirect("login")
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
        return redirect('login')

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        todo = form.save(commit=False)
        todo.user = user
        todo.save()
        return redirect("anotacoes", id_user=id_user)
    else:
        print(form.errors)

    context = {
        "user":user,
        "form":form,
    }
    return render (request, "editar.html", context)


@login_required()
def remover(request, id_user, id_anotacao):
    todo = get_object_or_404(Todo, id=id_anotacao)
    user = get_object_or_404(User, id=id_user)

    form = TodoForm(instance=todo)

    #Consertar com o login_required
    if request.user.id != id_user:
        return redirect('login')

    if request.method == "POST":
        todo.delete()
        return redirect("anotacoes", id_user=id_user)
    else:
        print(form.errors)
        return render (request, "delete.html", {"user":user, "tarefa":todo})


def apagar_imagem(request, id_user, id_imagem,id_anotacao):
    image = get_object_or_404(Image, id=id_imagem)
    user = get_object_or_404(User, id=id_user)
    todo = get_object_or_404(Todo, id=id_anotacao)

    form = ImageForm(instance=image)

    #Consertar com o login_required
    if request.user.id != id_user:
        return redirect('login')

    if request.method == "POST":
        image.delete()
        return redirect("show", id_user=id_user, id_anotacao=id_anotacao)
    else:
        print(form.errors)
    return render (request, "apagar_imagem.html", {"user":user, "imagem":image, "tarefa":todo})


def editar_descricao(request, id_user, id_imagem, id_anotacao):
    image = get_object_or_404(Image, id=id_imagem)
    user = get_object_or_404(User, id=id_user)
    todo = get_object_or_404(Todo, id=id_anotacao)
    form = ImageForm(request.POST, request.FILES, instance=image)

    #Consertar com o login_required
    if request.user.id != id_user:
        return redirect('login')

    if request.method == "POST":
        image = form.save(commit=False)
        image.user = todo
        image.save()

        return redirect("show", id_user=id_user, id_anotacao=id_anotacao)
    else:
        print(form.errors)

    context = {
        "user":user,
        "imagem":image,
        "tarefa":todo,
        "form":form
    }
    return render (request, "editar_descricao.html", context)
