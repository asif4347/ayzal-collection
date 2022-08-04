from django.contrib import admin
from . import models as coming_soon_models

# Register your models here.

admin.site.register(coming_soon_models.Subscription)
admin.site.register(coming_soon_models.Contacts)
