from django.core.management.base import BaseCommand

import csv
from datetime import datetime

from actors.models import Actors


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com nome dos atores.'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%d/%m/%Y').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actors.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality
                )

        self.stdout.write(self.style.SUCCESS('== ATORES CADASTRADOS COM SUCESSO! =='))
