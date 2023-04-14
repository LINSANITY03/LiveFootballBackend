import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from tournament.factories import TournamentFactory

register(TournamentFactory)


@pytest.fixture
def api_client(scope="session"):
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def user_1(db):
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    return {'username': 'john', 'password': 'johnpassword'}
