import pytest
import json

from talentmap_api.position.models import CapsuleDescription

from model_mommy import mommy
from rest_framework import status


@pytest.mark.django_db()
def test_capsule_description_creation(authorized_client, authorized_user):
    assert CapsuleDescription.objects.count() == 0

    response = authorized_client.post('/api/v1/capsule_description/', data=json.dumps(
        {
            "content": "Test content"
        }
    ), content_type='application/json')

    assert response.status_code == status.HTTP_201_CREATED
    assert CapsuleDescription.objects.count() == 1


@pytest.mark.django_db()
def test_capsule_description_update(authorized_client, authorized_user):
    mommy.make(CapsuleDescription, id=1, content="banana")

    response = authorized_client.patch('/api/v1/capsule_description/1/', data=json.dumps(
        {
            "content": "banana splits"
        }
    ), content_type='application/json')

    assert response.status_code == status.HTTP_200_OK
    assert CapsuleDescription.objects.get(id=1).content == "banana splits"