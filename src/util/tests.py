from django.test import TestCase

# Create your tests here.
from src.database.models import myUser, Members, Association
from .apps import CSVParser


class CSVParserTests(TestCase):

    def test___str__(self):
        test = CSVParser('../../misc/asso.csv')
        print(test)

    def test_to_database(self):
        test = CSVParser('/home/rod/projects/YakaChoisir/misc/asso.csv')
        test.to_database()
        print(myUser.objects.all())
        print(Members.objects.all())
        print(Association.objects.all())
