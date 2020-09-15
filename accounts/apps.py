from django.apps import AppConfig
from accounts import signals

class AccountsConfig(AppConfig):
    name = 'accounts'

    # def ready(self):
    #     import accounts.signals #signals


