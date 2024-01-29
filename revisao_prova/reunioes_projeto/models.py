from django.db import models

class Reuniao(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    local = models.CharField(max_length=80)
    nome_do_participante = models.CharField(max_length=120)
    dia = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return self.titulo