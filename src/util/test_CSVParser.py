from unittest import TestCase
from src.util.csv_parser import CSVParser


class TestCSVParser(TestCase):
    def test___str__(self):
        test = CSVParser('../../misc/asso.csv')
        print(test)

    def test_to_database(self):
        test = CSVParser('../../misc/asso.csv')
        print(test.to_database())
