from django.apps import AppConfig


class HelloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello'
    
    def ready(self):
        # Import signals to register them
        # Common error: importing signals but forgetting to call super().ready()
        import hello.signals  # This registers the signal handlers
