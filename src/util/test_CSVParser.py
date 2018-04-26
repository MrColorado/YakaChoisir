from unittest import TestCase

from src.database.models import Association, Members, myUser
from src.util.csv_parser import CSVParser


class TestCSVParser(TestCase):
    def test___str__(self):
        test = CSVParser('../../misc/asso.csv')
        print(test)

    def test_to_database(self):
        django.setup()
        test = CSVParser('../../misc/asso.csv')
        test.to_database()
        print(myUser.objects.all())
        print(Members.objects.all())
        print(Association.objects.all())
