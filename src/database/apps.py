from django.apps import AppConfig


class DatabaseConfig(AppConfig):
    name = 'database'

def load():
    parser = src.util.apps.CSVParser('/home/mrcolorado/YakaChoisir/misc/asso.csv')
    parser.to_database()

