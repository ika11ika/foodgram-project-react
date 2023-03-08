import csv
import os

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(os.getcwd())
        for filename in os.listdir(os.getcwd()):
            if filename == 'data':
                print(os.getcwd())
                for file in os.listdir(filename):
                    print(file)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.import_ingredients()
        print('Ингридиенты загружены!')

    def import_ingredients(self, file='ingredients.csv'):
        file_path = f'data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                status, created = Ingredient.objects.update_or_create(
                    name=row[0],
                    measurement_unit=row[1]
                )
