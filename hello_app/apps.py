from django.apps import AppConfig


class HelloAppConfig(AppConfig):
    name = 'hello_app'

    def ready(self):
        #recall service
        import hello_app.services.modelobjservice