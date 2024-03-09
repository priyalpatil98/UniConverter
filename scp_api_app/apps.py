from django.apps import AppConfig


class ScpApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scp_api_app'

class ScpApiAppConfigrest_framework(ScpApiAppConfig):
    name = 'scp_api_app'
