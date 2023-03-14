from django.contrib import admin
from .models import info
from .models import team

# Register your models here.
admin.site.register(info)
admin.site.register(team)