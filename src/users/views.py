from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib import messages


def _signup(request):
    if not request.user.is_authenticated:
        if request.method == "GET":
            form = UserCreationForm()
            return render(request, "pages/users/signup.html", {"form": form})

        else:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = User.objects.filter(username=form.cleaned_data['username'])
                if user.exists():
                    messages.info(request, 'Username já existe!')
                    return redirect(reverse('signup'))
                form.save()

                messages.add_message(request, messages.SUCCESS, "Your data is signed 😁")
                return redirect("login")
            messages.add_message(
                request, messages.ERROR, "Por favor, preencha correctamente o formulário!"
            )
            return redirect("signup")
    else:
        messages.info(request, 'Você já está logado!')
        return redirect(reverse('home'))


def _login(request):
    if not request.user.is_authenticated:
        if request.method == "GET":
            form = AuthenticationForm()
            return render(request, "pages/users/login.html", {"form": form})

        else:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                messages.success(request, "Loged 💖")
                return redirect(reverse("home"))
            messages.error(request, "Username ou senha inválidos!")
            return redirect("login")
    else:
        messages.info(request, 'Você já está logado!')
        return redirect(reverse('home'))


def _logout(request):
    if request.user.is_authenticated:
        logout(request)

        messages.success(request, "Deslogado com sucesso, volte sempre 😭")
        return redirect(reverse("login"))
    messages.info(request, 'Você não está logado!')
    return redirect(reverse('login'))
