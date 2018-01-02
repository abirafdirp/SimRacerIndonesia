import csv
import uuid

import datetime
from allauth.account.models import EmailAddress
from cities_light.models import City, Country
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from simracerindonesia.core.models import RacingSimulator
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
            lines = f.read().splitlines()

        User.objects.all().exclude(username='admin123').delete()

        lines = csv.reader(lines, delimiter=',')
        for line in lines:
            try:
                if int(line[0]) != 1:
                    continue
            # if line is empty
            except ValueError:
                continue

            name = line[2]
            country_from_file = line[5].strip()
            city_from_file = line[6].strip()
            gender = line[7]
            birth_year = line[8]
            racing_simulators = line[9]
            experience = line[10]
            real_experience = line[11]
            highest_achievement = line[12]
            favourite_cars = line[13]
            hardware = line[14]
            email = line[15]

            username = email.split('@')[0]

            user = User(name=name, username=username, email=email)
            user.set_password(uuid.uuid4())

            try:
                user.save()
            except IntegrityError:
                print(username)
                raise

            user.profile.gender = gender

            if birth_year != '-' and birth_year != '':
                user.profile.birth_year = datetime.date(
                    year=int(birth_year), month=1, day=1
                )

            user.profile.simracing_experience = experience

            if real_experience == 'Yes':
                user.profile.real_life_racing_experience = True
            else:
                user.profile.real_life_racing_experience = False

            user.profile.highest_simracing_achievement = highest_achievement
            user.profile.favourite_cars = favourite_cars
            user.profile.hardware = hardware

            if racing_simulators != '-':
                racing_simulators = racing_simulators.split(', ')
                for racing_simulator in racing_simulators:
                    racing_simulator, created = RacingSimulator.objects.get_or_create(
                        name=racing_simulator
                    )
                    user.profile.racing_simulators.add(racing_simulator)

            try:
                cities = City.objects.filter(
                    name_ascii__iexact=city_from_file,
                    country__name_ascii__iexact=country_from_file
                ).order_by('-population')
            except City.DoesNotExist:
                not_city = True
            else:
                if cities:
                    not_city = False
                    user.profile.city = cities[0]
                else:
                    not_city = True

            if not_city:
                try:
                    country = Country.objects.get(
                        name_ascii__iexact=country_from_file
                    )
                except Country.DoesNotExist:
                    user.profile.country_freetext = country_from_file
                else:
                    user.profile.country = country

            if not_city:
                user.profile.city_freetext = city_from_file

            user.profile.save()

            EmailAddress.objects.create(
                user=user, email=email, verified=True, primary=True
            )
