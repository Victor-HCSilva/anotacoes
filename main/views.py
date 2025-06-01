from django.shortcuts import render
from init.models import Todo, User
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from init.forms import TodoForm


@login_required
def anotacoes(request, id_user):
    if request.user.id != id_user:
        return redirect('login')

    #todos = get_your_task(id_user)
    #todos = Todo.objects.filter(id=id_user)
    todos = Todo.objects.all()

    context = {
        "anotacoes":todos,
    }
    return render(request, "anotacoes.html", context)


def show(request, id_user,id_anotacao):
    if request.user.id != id_user:
        return redirect("login")
    task = get_object_or_404(Todo, id=id_anotacao)
    user = get_object_or_404(User, id=id_user)
    context = {
        "tarefa":task,
        "user": user,
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
        return redirect("main", id_user=id_user)
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
        return redirect("main", id_user=id_user)
    else:
        print(form.errors)
        return render (request, "delete.html", {"user":user, "tarefa":todo})
