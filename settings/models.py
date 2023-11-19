from django.db import models

class Setting(models.Model):
    schedule_start = models.TimeField()
    schedule_end = models.TimeField()
    start_by_time = models.BooleanField()
    is_open = models.BooleanField(default=False)

    @classmethod
    def get_setting(cls, **kwargs):
        setting, created = Setting.objects.get_or_create(defaults=kwargs, pk=1)

        if created:
            setting.save()

        return setting

    def is_open_now(self):
        return self.is_open