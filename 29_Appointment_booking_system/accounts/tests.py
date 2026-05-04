from django.test import TestCase
from .models import User, ConsultancyMember
from consultancy.models import Consultancy
from .serializer import UserSerializer

# Create your tests here.
class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="TestUser1", email="testuser1@gmail.com", password="admin@123")

    def test_user_got_created(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, "TestUser1")

class SerialzerTest(TestCase):
    def test_serializer_is_valid(self):
        data = {
            "username": "TestUser1",
            "email": "testuser1@gmail.com",
            "password": "admin@123 "
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
    
    def test_serializer_is_invalid(self):
        data = {
            "username": "",
            "email": "testuser1@gmail.com",
            "password": "admin@123 "
        }
        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class ConsultancyMemberTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="TestUser1", email="testuser1@gmail.com", password="admin@123")
        Consultancy.objects.create(title="Consultancy1", description="Some random description")
        ConsultancyMember.objects.create(user_id=1, consultancy_id=1)
    
    def test_consultancy_member_model(self):
        self.assertEqual(ConsultancyMember.objects.get(id=1).user_id, 1)
        