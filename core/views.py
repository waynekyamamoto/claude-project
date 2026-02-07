import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import RegistrationForm
from .models import AdderGame, AdderQuestion


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def level2(request):
    return render(request, 'level2.html')


@login_required
def towers(request):
    return render(request, 'towers.html')


@login_required
def adder(request):
    return render(request, 'adder.html')


@login_required
@require_POST
def adder_save(request):
    data = json.loads(request.body)
    game = AdderGame.objects.create(
        user=request.user,
        score=data['score'],
        total=data['total'],
    )
    for q in data['questions']:
        AdderQuestion.objects.create(
            game=game,
            num1=q['num1'],
            num2=q['num2'],
            user_answer=q['user_answer'],
            correct=q['correct'],
        )
    return JsonResponse({'status': 'ok', 'game_id': game.id})


@login_required
def adder_history(request):
    games = AdderGame.objects.filter(user=request.user).order_by('-played_at')
    return render(request, 'adder_history.html', {'games': games})


@login_required
def account_settings(request):
    return render(request, 'account_settings.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
