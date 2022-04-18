from django.contrib import admin
from .models import linguagems_progr, linguagens_mais_usadas
from .models_2.projetos import projeto

admin.site.register(linguagems_progr)
admin.site.register(linguagens_mais_usadas)
admin.site.register(projeto)
