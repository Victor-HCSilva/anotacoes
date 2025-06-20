from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Todo
from django.contrib.auth import logout


@login_required()
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #messages.success(request, 'Login realizado com sucesso!')
            return redirect('welcome', id_user=user.id)
        else:
            #messages.error(request, 'CPF ou senha inválidos!')
            print(user)
            return render(request, 'login.html')
    else:
        return render (request, "login.html")


@login_required()
def main(request, id_user: int):
    todos = Todo.objects.filter(user=get_object_or_404(User, id=id_user))
    form = TodoForm()
    user = get_object_or_404(User, id=id_user)

    #Consertar com o login_required
    if request.user.id != id_user:
        return redirect('login')

    if request.method == "POST":
        form = TodoForm(request.POST)
        todo = form.save(commit=False)
        todo.user = user
        todo.save()
        return redirect("anotacoes", id_user=id_user)
    else:
        print(form.errors)

    context = {
        "username":user.username.title(),
        "todos":todos,
        "form":form,
    }
    return render(request, "main.html",context)


@login_required()
def welcome(request, id_user):
    if request.user.id != id_user:
        return redirect("login")

    user = get_object_or_404(User, id=id_user)
    todos = Todo.objects.filter(user=get_object_or_404(User, id=id_user))
    nick = user.username if user.username is not None else "User"
    context = {
        "nick":"nick",
        "todos":todos,
        "user":user,
    }
    return render(request, "welcome.html", context)


def sobre(request):
    user = get_object_or_404(User, id=request.user.id)
    return render(request, "sobre.html",{"user":user})

def logout_(request):
    logout(request)
    return redirect("login")
