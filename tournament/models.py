from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime
# Create your models here.


class TOURNA_CHOICES(models.IntegerChoices):
    SM = 2, '2'
    MD = 4, '4'
    XL = 8, '8'


class GAMETIME_CHOICES(models.IntegerChoices):
    QUICK = 5, '5'
    NORMAL = 10, '10'
    LONG = 20, '20'


class STATUS_CHOICES(models.IntegerChoices):
    TBD = 0, 'TBD'
    ON_GOING = 1, 'Ongoing'
    DONE = 2, 'Completed'


class Tournament(models.Model):

    class Meta:
        db_table = 'Tournament'

    name = models.CharField(blank=False, null=False, max_length=50)
    photo_img = models.ImageField(
        blank=True, null=True, upload_to='photos/tournament')
    total_games = models.IntegerField(blank=False, null=False, default=0)
    total_teams = models.IntegerField(
        choices=TOURNA_CHOICES.choices, default=TOURNA_CHOICES.SM)
    time_games = models.IntegerField(
        choices=GAMETIME_CHOICES.choices, default=GAMETIME_CHOICES.QUICK)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return self.name


class Teams(models.Model):
    class Meta:
        db_table = 'Teams'

    name = models.CharField(blank=False, null=False, max_length=50)
    photo_img = models.ImageField(
        blank=True, null=True, upload_to='photos/teams')
    tournament = models.ForeignKey(Tournament, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return self.name


class Players(models.Model):
    class Meta:
        db_table = 'Players'

    name = models.CharField(blank=False, null=False, max_length=50)
    team = models.ForeignKey(
        Teams, on_delete=models.DO_NOTHING, related_name='team')
    photo_img = models.ImageField(
        blank=True, null=True, upload_to=f'photos/{team}')
    jersey_no = models.IntegerField(
        validators=[MaxValueValidator(99), MinValueValidator(1)], default=1, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return f'{self.name} from {self.team} FC'


class Games(models.Model):

    class Meta:
        db_table = 'GamesHistory'

    home_team = models.ForeignKey(
        Teams, on_delete=models.DO_NOTHING, related_name='hometeam')
    away_team = models.ForeignKey(
        Teams, on_delete=models.DO_NOTHING, related_name='awayteam')
    created_at = models.DateTimeField(default=datetime.datetime.now)
    status = models.IntegerField(
        choices=STATUS_CHOICES.choices, default=STATUS_CHOICES.TBD)

    def __str__(self) -> str:
        return f'{self.home_team} vs {self.away_team}'
