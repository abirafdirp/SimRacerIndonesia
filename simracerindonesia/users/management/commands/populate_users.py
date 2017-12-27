from django.core.management.base import BaseCommand

from simracerindonesia.users.models import User
from simracerindonesia.utils.file_location import get_full_path


class Command(BaseCommand):
    help = "Populate users from member_list.csv in Users fixtures folder"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(
            'Populating....'
        ))

        file_path = get_full_path(
            'simracerindonesia/users/fixtures/member_list.csv'
        )
        with open(file_path, encoding='utf-8') as f:
            lines = f.read().replace(',', '').splitlines()

        for line in lines:
            if int(line[0]) != 1:
                continue

            name = line[2]
            country = line[5]
            city = line[6]
            gender = line[7]
            birth_year = line[8]
            racing_simulator = line[9]
            experience = line[10]
            real_experience = line[11]
            highest_achievement = line[12]
