from mock import patch

def test_user_list(client):

    #make user object
    #maybe its a db
    user = UserFactory.build()
    #monkeypatching
    with patch.object(UserDetailView, 'get_object', return_value=user):
         #when calling the DetailView for this object
         url = reverse('detail', kwargs={'pk':1234})
         response = client.get(url)
         content = response.content.decode()

         assert response.status_code == 200
         assert str(user.models) in content