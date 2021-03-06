from django.shortcuts import render

from stats import models


def home_view(request):
    """
    Home page
    """

    teams = models.TeamModel.objects.all()
    return render(request, 'stats/home.html', {'teams': teams})


def team_players_view(request, team_id):
    """
    Players of each team
    """
    players = models.PlayerModel.objects.filter(team_id=team_id)
    return render(request, 'stats/team_players.html', {'players': players})


def player_stats_view(request, player_id=None):
    """
    Stats of each player
    """

    player = models.PlayerModel.objects.get(id=player_id)
    return render(request, 'stats/player_stats.html', {'player': player})

