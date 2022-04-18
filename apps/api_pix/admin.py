from django.contrib import admin
from .models import Charge
# Register your models here.
@admin.register(Charge)
class Change_Usuario_Admin(admin.ModelAdmin):
    list_display = ('user', 'value', 'status', 'created', 'updated')
    search_fields = ['status', 'value']
    list_filter = ['user', 'status', 'created']
    save_on_top = True