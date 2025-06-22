from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Todo
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


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
        return redirect("main:anotacoes", id_user=id_user)
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
        return redirect("main:login")

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



# Login do django mesmo
class CustomLoginView(LoginView):
    """
    Uma view de login customizada para redirecionar o usuário para a sua
    página de boas-vindas, que requer o ID do usuário como argumento.
    """
    # Especifique o nome do seu template de login aqui.
    template_name = 'login.html' # SUBSTITUA PELO NOME DO SEU ARQUIVO

    def get_success_url(self):
        """
        Este método é chamado após um login bem-sucedido.
        Ele constrói a URL de redirecionamento dinamicamente.
        """
        # 1. Pega o usuário que acabou de fazer o login.
        user = self.request.user

        # 2. Usa 'reverse_lazy' para construir a URL de forma segura,
        #    passando o ID do usuário como um argumento (kwargs).
        #    'welcome' deve ser o 'name' da sua URL no arquivo urls.py.
        return reverse_lazy('welcome', kwargs={'id_user': user.id})
