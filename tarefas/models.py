from datetime import date

from django.db import models

class Tarefas(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False, verbose_name="Título")
    data_inicio = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name="Data Inicio")
    data_final = models.DateField(null=False, blank=False, verbose_name="Data Final")
    data_terminada = models.DateField(null=True)

    class Meta:
        ordering = ["data_final"]

    def marque_como_finalizado(self):
        if not self.data_terminada:
            self.data_terminada = date.today()
            self.save()