from django.contrib import admin
from .models import Tournament, Teams, Players, Games

# Register your models here.

admin.site.register(Tournament)
admin.site.register(Teams)
admin.site.register(Players)
admin.site.register(Games)
