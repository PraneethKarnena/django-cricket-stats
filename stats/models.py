from django.db import models


class TeamModel(models.Model):
    """
    Database table for Team.
    Contains Team details.
    """

    name = models.CharField(max_length=255, null=False, blank=False)
    logo = models.ImageField(null=False, blank=False)
    club_state = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.club_state}'