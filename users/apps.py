from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Call constructor in to users
    def ready(self):
        import users.signals
