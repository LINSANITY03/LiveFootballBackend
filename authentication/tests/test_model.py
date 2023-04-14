import pytest
from django.contrib.auth.models import User

# function Run once per test
# class    Run once per class of tests
# module   Run once per module
# session  Run once per session


@pytest.mark.skip
def test_example():
    assert 1 == 1


@pytest.fixture
def fixture_1(scope="session"):
    print('run-fixture-1')
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    return 1


@pytest.mark.django_db
def test_user_count(fixture_1):
    num = fixture_1
    assert User.objects.count() == num
