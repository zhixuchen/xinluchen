from django.contrib import admin
from Customer_profile.models import Customer
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(ImportExportActionModelAdmin):
    list_display = ['licence_plate', 'name', 'mobile']
    list_display_links = list_display
    search_fields = list_display


admin.site.site_title = '鑫路臣'
admin.site.site_header = '鑫路臣'
