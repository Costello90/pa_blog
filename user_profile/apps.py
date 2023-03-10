from django.apps import AppConfig


class ProfilesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'

    def ready(self):
        from user_profile import signals
