from django.contrib import admin

# Register your models here.

from .models import Meaning
 
class MeaningAdmin(admin.ModelAdmin):
    list_display = ("word", "mean",)

admin.site.register(Meaning, MeaningAdmin)