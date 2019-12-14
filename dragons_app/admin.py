from django.contrib import admin
from dragons_app import models

# Register your models here.

admin.site.register(models.Rule)
admin.site.register(models.Dragon)
admin.site.register(models.DragonKillRecord)