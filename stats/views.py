from django.shortcuts import render

from stats import models


def home_view(request):
    """
    Home page
    """

    teams = models.TeamModel.objects.all()
    return render(request, 'stats/home.html', {'teams': teams})