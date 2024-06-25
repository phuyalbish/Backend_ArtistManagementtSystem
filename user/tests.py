# from django.test import TestCase
# from .models import Users

# # class MyModelTest(TestCase):

# #     # def setUp(self):
# #     #     pass  
        
# #     def test_equal(self):
# #         self.assertEqual(1, 2) 

# class UsersModelTestCase(TestCase):
    
#     def test_gender_choices(self):
#         user = Users.objects.create(email='test@example.com', username='testuser')
        
#         # user.gender = 0
#         # self.assertEqual(user.get_gender_display(), 'Male')
        
#         # user.gender = 1
#         # self.assertEqual(user.get_gender_display(), 'Female')
        
#         user.gender = 4
#         self.assertEqual(user.get_gender_display(), 'Others')
        
# from django.test import TestCase
# from rest_framework.test import APITestCase
# from rest_framework import status
# from .models import Users

# class PostUserTest(APITestCase):
#     def setUp(self):
#         self.user_data = {
#             'username': 'testuser',
#             'password': 'testpassword',
#             'email': 'testuser@example.com',
#             'is_staff': True
#         }

#     def test_post_user(self):
        
#         response = self.client.post('/api/user/post/', data=self.user_data, format='json')

       
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
# from django.test import TestCase
# from rest_framework.test import APITestCase
# from rest_framework import status
# from .models import Users

# class PostUserTest(APITestCase):
#     def setUp(self):
#         self.user_data = {
#             'username': 'testusername',
#             'password': 'testpassword',
#             'email': 'testuser1222@example.com',
#             'is_staff': True
#         }

#     def test_post_user(self):
     
#         response = self.client.post('/api/user/post/', data=self.user_data, format='json')
        
    
#         self.assertEqual(response.status_code, status.HTTP_403_CREATED)
        
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Users  
from .serializers import UserSerializer  
from django.urls import reverse

class GetStaffTestCase(TestCase):
    def setUp(self):
     
        self.user1 = Users.objects.create(username='user1',email='nppp@gmail.com', is_deleted=False, is_staff=True, is_superuser=False)
        self.user2 = Users.objects.create(username='user2',email='nppp2@gmail.com', is_deleted=False, is_staff=True, is_superuser=False)
        self.user3 = Users.objects.create(username='user3',email='nppp3@gmail.com', is_deleted=True, is_staff=True, is_superuser=False)

        self.client = APIClient()

    def test_get_staff_success(self):
        url = reverse('get_staff')  
        response = self.client.get('/api/staff/get/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  
        
    
    

    # def test_get_staff_no_results(self):
      
    #     Users.objects.filter(is_staff=True).update(is_deleted=True)  

    #     url = reverse('/api/staff/get') 
    #     response = self.client.get(url)

    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    #     self.assertEqual(response.data['detail'], 'No Staff Found')

   
