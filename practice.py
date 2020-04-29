#practice pytest

import pytest

@pytest.mark.django_db
def test_user_list(client):

    user = UserFactory.create()
    url = reverse('user', kwargs={'user_id': 1})
    response = client.get(url)
    content = response.content.decode()

    assert response.status_code == 200
    assert str(user.models) in content

    