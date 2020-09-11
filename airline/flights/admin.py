from django.contrib import admin

from .models import Airport, Flight
# Register your models here.
# Register models to the admin site in order to access it in admin site
admin.site.register(Airport)
admin.site.register(Flight)