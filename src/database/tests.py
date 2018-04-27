from django.contrib.auth.models import User

from util.apps import CSVParser
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

    def test_csvParserPrint(self):
        parser = CSVParser('/home/rod/projects/YakaChoisir/misc/asso.csv')
        print(parser)

    def test_csvParserWriteDB(self):
        parser = CSVParser('/home/rod/projects/YakaChoisir/misc/asso.csv')
        parser.to_database()
        print(myUser.objects.all())
        print(Association.objects.all())
        print(Members.objects.all())
