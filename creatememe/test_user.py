import datetime as dt  

from django import urls
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session   
from django_dynamic_fixture import G  
#from django.urls import reverse  
import freezegun
import pytest  

@pytest.mark.parametrize('view_name', ['user:register', 'user:login'])
def test_public_views(view_name, client):

    url = urls.reverse(view_name)
    response = client.get(url)
    assert response.status_code == 200 
    
@freezegun.freeze_time('2020-04-20 7:00:00')
@pytest.mark.django_db
def test_register(client):
    register_url = urls.reverse('user:register')
    response = client.post(register_url, {
        'username': 'my_username',
        'password1': 'my_password123',
        'password2': 'my_password123'

    })
    #the registration view should redirect us to our homepage
    assert response.status_code == 302
    assert response.url == urls.reverse('home')
    #there should be a user with my_username
    user = User.objects.get(username='my_username')
    assert user.last_login == dt.datetime(2020, 4, 20, 7)

@pytest.mark.django_db
def test_login_and_logout(client):
    user = G(User, username='my_username')
    user.set_password('my_password123')
    user.save()

    login_url = urls.reverse('user:login')
    response = client.post(login_url, {
        'username':'my_username',
        'password': 'my_password123'
    })
    #login url should redirect to the homepage
    assert response.status_code == 302
    assert response.url == urls.reverse('home')
    #logged in users have a session created for them
    assert Session.objects.count() ==1

    # log out the user
    logout_url = urls.reverse('user:logout') 
    response = client.get(logout_url)

    #similar to the login view, the logout view redirects to the login page
    assert response.status_code == 302
    assert response.url == urls.reverse('user:login')
    #there should be no sessions left after logging out  
    assert not Session.objects.exists()    