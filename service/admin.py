from django.contrib import admin, sites
from service.models import Service


# Register your models here.

class Service_admin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'description')


admin.site.register(Service, Service_admin)
