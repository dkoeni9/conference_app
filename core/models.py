from datetime import datetime, date, timedelta
from django.db import models
from django.utils import timezone


class Speaker(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО докладчика")
    topic = models.CharField(max_length=300, verbose_name="Тема выступления")
    duration = models.DurationField(help_text="ЧЧ:ММ:СС или ММ:СС")

    def __str__(self):
        return f'{self.full_name.split()[0]} {self.full_name.split()[1][0]}.{self.full_name.split()[2][0]}. — "{self.topic}"'


class Conference(models.Model):
    speaker = models.ForeignKey(
        Speaker, on_delete=models.SET_NULL, null=True, blank=True
    )
    start_time = models.TimeField(null=True, blank=True)
    is_running = models.BooleanField(default=False)
    extra_time = models.DurationField(
        default=0, help_text="Дополнительное время в формате ЧЧ:ММ:СС"
    )

    def calculate_remaining_time(self):
        if not self.speaker or not self.start_time or not self.is_running:
            return None

        start_datetime = datetime.combine(date.today(), self.start_time)
        start_datetime = timezone.make_aware(
            start_datetime, timezone.get_current_timezone()
        )

        total_seconds = (self.speaker.duration + self.extra_time).total_seconds()
        elapsed = (timezone.now() - start_datetime).total_seconds()
        return int(total_seconds - elapsed)

    def __str__(self):
        return f"Выступает: {self.speaker}"

    class Meta:
        verbose_name_plural = "Conference"
