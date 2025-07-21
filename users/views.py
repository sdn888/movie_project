from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('film_list')  # куда перенаправлять после регистрации

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # автоавторизация
        messages.success(self.request, "Добро пожаловать, вы успешно зарегистрированы!")
        return super().form_valid(form)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно. Теперь войдите.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
