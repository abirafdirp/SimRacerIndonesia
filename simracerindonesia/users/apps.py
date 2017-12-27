from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'simracerindonesia.users'
    verbose_name = "Users"

    def ready(self):
        import simracerindonesia.users.signals
