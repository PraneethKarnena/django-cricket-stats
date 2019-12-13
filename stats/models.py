from django.db import models


class TeamModel(models.Model):
    """
    Database table for Team.
    Contains Team details.
    """

    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    logo = models.ImageField(null=False, blank=False)
    club_state = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.club_state}'


# class PlayerModel(models.Model):
#     """
#     Database table for info of the player.
#     Contains individual stats and details of the player.
#     """

#     first_name = models.CharField(max_length=255, null=False, blank=False)
#     last_name = models.CharField(max_length=255, null=False, blank=False)

#     image = models.ImageField(null=False, blank=False)
#     jersey_num = models.PositiveSmallIntegerField(null=False, blank=False)
#     country = models.CharField(max_length=255, null=False, blank=False)

#     matches = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
#     runs = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
#     highest_score = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
#     fifties = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
#     hundreds = models.PositiveSmallIntegerField(default=0, null=False, blank=False)

#     team = models.ForeignKey(TeamModel, on_delete=models.CASCADE, null=False, blank=False)

#     def __str__(self):
#         return f''

