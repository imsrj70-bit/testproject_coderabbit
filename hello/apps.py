from django.apps import AppConfig


class HelloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello'
    
    def ready(self):
        # Import signals to register them
        # Common error: importing signals but forgetting to call super().ready()
        """
        Run app startup tasks and register the app's signal handlers.
        
        Imports the hello.signals module to ensure its signal handlers are registered when the Django app is ready. This import is performed for its side effect of registering signals during app initialization.
        """
        import hello.signals  # This registers the signal handlers