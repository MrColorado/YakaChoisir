from django.test import TestCase

# Create your tests here.
from database.models import myUser, Members, Association
from .apps import CSVParser


class CSVParserTests(TestCase):

    def test___str__(self):
        test = CSVParser('../misc/asso.csv')
        print(test)

    def test_write_database(self):
        test = CSVParser('../misc/asso.csv')
        test.to_database()
        print(myUser.objects.all())
        print(Members.objects.all())
        print(Association.objects.all())

    def test_trim_email(self):
        email_ok = 'pass@domain.com'
        email_fail = 'pass@domain.com;'
        self.assertEqual(email_ok, CSVParser.trim_email(email_ok))
        self.assertEqual(email_ok, CSVParser.trim_email(email_fail))
        self.assertEqual(None, CSVParser.trim_email(None))
