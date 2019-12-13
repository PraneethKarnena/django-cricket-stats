from django.contrib import admin

from stats import models


admin.site.register(models.PlayerModel)
admin.site.register(models.MatchModel)
admin.site.register(models.TeamModel)
