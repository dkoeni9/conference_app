from django import forms
from django.contrib import admin
from .models import Speaker, Conference


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "topic", "duration")
    search_fields = ("full_name", "topic")


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ("speaker", "start_time", "is_running", "extra_time")
    list_editable = ("is_running", "extra_time")

    def has_add_permission(self, request):
        if Conference.objects.exists():
            return False
        return super().has_add_permission(request)


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = "__all__"
        widgets = {"start_time": forms.TimeInput(format="%H:%M")}
