import pytest
from django.contrib.auth.models import User


@pytest.fixture
def api_client(scope="session"):
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def user_1(db):
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    return {'username': 'john', 'password': 'johnpassword'}
