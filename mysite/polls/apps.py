from django.apps import AppConfig

# from .signals import save_profile


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'

    def ready(self):
        import polls.signals



