from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "jazmin_leon_llc.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
