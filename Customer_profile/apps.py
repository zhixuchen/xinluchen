from django.apps import AppConfig


class CustomerProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Customer_profile'
    verbose_name="客户档案"
    verbose_name_plural=verbose_name
