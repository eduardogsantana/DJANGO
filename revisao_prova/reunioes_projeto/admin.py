from django.contrib import admin
from .models import Reuniao

class ReuniaoList(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'local', 'nome_do_participante', 'dia', 'horario']

admin.site.register(Reuniao)
