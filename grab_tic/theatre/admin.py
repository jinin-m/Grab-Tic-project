from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Place)

admin.site.register(models.Theatre)

admin.site.register(models.Screen)

admin.site.register(models.ShowDate)

admin.site.register(models.ShowTime)

admin.site.register(models.OngoingShows)

admin.site.register(models.ScreenDateTime)

admin.site.register(models.Seat)

admin.site.register(models.Bookings)
