from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # 导入 并注册到后台
from .models import UserProfile
from django.utils.translation import gettext_lazy


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = ['username', 'last_name', 'first_name']
    list_display_links = list_display
    search_fields = list_display
    add_fieldsets = (
        (None, {u'fields': ('username', 'password1', 'password2')}),
        (gettext_lazy('User Information'), {'fields': ('mobile', 'email')}),
    )
