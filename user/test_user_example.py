import requests
import pytest
import json
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_409_CONFLICT,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_403_FORBIDDEN,
    HTTP_423_LOCKED,
) 

pytestmark = [pytest.mark.django_db, ]

class TestUserList:
    def test_user_list_get(self, logger, headers, api_client):
        ret = api_client.get('/users/', headers=headers)
        logger.info(ret)
        assert ret.status_code == HTTP_200_OK

    def test_user_list_post(self, logger, headers, api_client):
        body = {
            "user_id": "yerin",
            "password": "1234",
            "name": "yerin",
            "email": "yerin@yerin.com"

        }
        ret = api_client.post('/users/', headers=headers, data=body)

        assert ret.status_code == HTTP_200_OK
        assert 'id' in ret.json()

    def test_user_list_delete(self, logger, headers, api_client):
        body = {
            'id': [
                1
            ]
        }
        ret = api_client.delete('/users/', headers=headers, data=body)
        assert ret.status_code == HTTP_204_NO_CONTENT


    @pytest.mark.parametrize("http_method", [
            "head",
            "put",
            "trace",
            "patch"
        ])
    
    def test_user_list_others(self, logger, headers, api_client, http_method):
        ret = getattr(api_client, http_method)('/users/', headers=headers)

        assert ret.status_code == HTTP_405_METHOD_NOT_ALLOWED
        
#여기서부터 수정 
class TestUser:
    def test_user_get(self, logger, headers, api_client):
        ret = api_client.get('/users/'user_id'', headers=headers)
        logger.info(ret)
        assert ret.status_code == 200

    def test_user_patch(self, logger, headers, api_client):
        pass

    @pytest.mark.parametrize("http_method", [
        "head",
        "put",
        "trace",
        "post"
    ])
    def test_user_others(self, logger, headers, api_client, http_method):
        pass

class TestUserFavorite:
    def test_user_favorite_get(self, logger, headers, api_client):
        pass

    def test_user_favorite_post(self, logger, headers, api_client):
        pass

    def test_user_favorite_delete(self, logger, headers, api_client):
        pass

    



