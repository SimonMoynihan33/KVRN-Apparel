from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    Configuration class for the 'bag' application.

    Sets the default auto field for model primary keys and registers
    the application under the name 'bag'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
