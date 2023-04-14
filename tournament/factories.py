import factory
from faker import Faker
from tournament.models import Tournament

fake = Faker()


class TournamentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tournament

    name = fake.name()
    total_games = 12
    total_teams = 4
    time_games = 30
    photo_img = factory.django.ImageField()
