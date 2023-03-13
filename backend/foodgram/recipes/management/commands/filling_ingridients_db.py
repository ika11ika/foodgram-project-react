import csv
import os
from pathlib import Path

from django.core.management.base import BaseCommand

from foodgram.settings import BASE_DIR
from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = Path(BASE_DIR + '/data')
        os.chdir(path)
        self.import_ingredients()
        self.stdout.write('Ингридиенты загружены!')

    def import_ingredients(self, file='ingredients.csv'):
        file_path = f'{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            ingrs_list = [
                Ingredient(
                    name=row[0],
                    measurement_unit=row[1]
                )
                for row in reader
            ]
            Ingredient.objects.bulk_create(
                ingrs_list,
                batch_size = 500
            )
