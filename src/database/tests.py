from django.contrib.auth.models import User
import django.db

from .models import myUser, Association, Members
from django.test import TestCase


# Create your tests here.

class MyUserTests(TestCase):

    def test_createUser(self):
        user = User.objects.create_user('MyUsername')
        self.assertEqual(user.username, 'MyUsername')

        userExtend = myUser()
        userExtend.user = user
        userExtend.mail_secondary = 'hello@gmail.com'

        self.assertEqual(userExtend.mail_secondary, 'hello@gmail.com')
