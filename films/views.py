from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required

def film_list(request):
    films = Film.objects.all().order_by('-created_at')
    return render(request, 'films/film_list.html', {'films': films})

@login_required
def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save(commit=False)
            film.author = request.user
            film.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})


