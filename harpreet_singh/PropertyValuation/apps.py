from django.apps import AppConfig


class PropertyvaluationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PropertyValuation'

    def ready(self):
        import PropertyValuation.signals

