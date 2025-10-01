from django.db import models


class Speaker(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО докладчика")
    topic = models.CharField(max_length=300, verbose_name="Тема выступления")
    duration = models.PositiveIntegerField(default=5, verbose_name="Длительность (мин)")

    def __str__(self):
        return f'{self.full_name} — "{self.topic}"'
