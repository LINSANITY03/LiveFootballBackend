import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_tournament_list(api_client, tournament_factory):
    tournament_factory.create()
    response = api_client.get(
        reverse('tournament-list')
    )
    print(response.content)
    assert response.status_code == 200
