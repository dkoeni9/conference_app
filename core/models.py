from django.db import models
from django.utils import timezone


class Speaker(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО докладчика")
    topic = models.CharField(max_length=300, verbose_name="Тема выступления")
    duration = models.PositiveIntegerField(default=5, verbose_name="Длительность (мин)")

    def __str__(self):
        return f'{self.full_name} — "{self.topic}"'


class Conference(models.Model):
    speaker = models.ForeignKey(
        Speaker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Текущий докладчик",
    )
    start_time = models.DateTimeField(
        null=True, blank=True, verbose_name="Время старта"
    )
    is_running = models.BooleanField(default=False, verbose_name="Таймер запущен")
    extra_time = models.IntegerField(
        default=0, verbose_name="Дополнительное время (сек)"
    )

    def calculate_remaining_time(self):
        if not self.speaker or not self.start_time:
            return None
        total_seconds = self.speaker.duration * 60 + self.extra_time
        elapsed = (timezone.now() - self.start_time).total_seconds()
        return int(total_seconds - elapsed)
