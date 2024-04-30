from django.contrib import admin
from todoapp import models

# Register your models here.

class admintask(admin.ModelAdmin):
    list_display = ("Title", "Time", "Complete", "Deleted")

admin.site.register(models.task, admintask)