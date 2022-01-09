from django.apps import AppConfig


class StaffInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Staff_info'
    verbose_name = "员工信息"
    verbose_name_plural = verbose_name
