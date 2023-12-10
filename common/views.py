from django.shortcuts import render
from . import models


def home(request):
    context = {
        'clubs': models.Club.objects.all(),
        'players': models.Player.objects.all(),
        'footer': models.Footer.objects.all()
    }
    return render(request, 'index.html', context=context)
