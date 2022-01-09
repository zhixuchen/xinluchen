from django.contrib import admin
from Customer_profile.models import *


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['licence_plate', 'name', 'mobile']
    list_display_links = list_display
    search_fields = list_display


admin.site.register(Customer, CustomerAdmin)

admin.site.site_title = '鑫路臣'
admin.site.site_header = '鑫路臣'
