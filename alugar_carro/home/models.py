from django.db import models

class AlugarCarro(models.Model):
    modelo = models.CharField(max_length=120, blank=False)
    foto = models.ImageField(upload_to='home')
    descricao = models.TextField(blank=True, null=True)
    ano_fabricacao = models.IntegerField()
    valor = models.FloatField()
    avaliacao = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.modelo


