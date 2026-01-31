from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Movies)

admin.site.register(models.Certification)

admin.site.register(models.Language)

admin.site.register(models.Cast)

admin.site.register(models.Genre)
