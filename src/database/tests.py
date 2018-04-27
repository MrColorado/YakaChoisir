from django.contrib.auth.models import User
from .models import myUser
from django.test import TestCase


# Create your tests here.

class myUserTests(TestCase):

    def createUserTest(self):
        user = User.objects.create_user('MyUsername')
        self.assertEqual(user.username, 'MyUsername')

        userExtend = myUser()
        userExtend.user = user
        userExtend.mail_secondary = 'hello@gmail.com'

        self.assertEqual(userExtend.mail_secondary, 'hello@gmail.com')
