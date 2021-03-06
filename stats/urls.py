from django.urls import path

from stats import views


urlpatterns = [
    path('', views.home_view),
    path('team-players/<int:team_id>/', views.team_players_view),
    path('player-stats/<int:player_id>/', views.player_stats_view),
]