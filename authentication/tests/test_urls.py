import json
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request(user_1, api_client):
    response = api_client.post(
        reverse('token_obtain_pair'), data=user_1
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_user(api_client):
    response = api_client.post(
        reverse('signup'), data={'username': 'john', 'password': 'johnpassword'}
    )
    assert response.status_code == 201
    assert json.loads(response.content) == "User has been created!"
