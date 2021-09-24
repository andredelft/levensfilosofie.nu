from django.db import models
from django.template.defaultfilters import slugify


class Symposium(models.Model):

    SLUG_LENGTH = 200

    title = models.CharField(max_length=300)
    introduction = models.TextField(null=True, blank=True)
    date = models.DateField(unique=True)
    time_from = models.TimeField(null=True, blank=True)
    time_to = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=200, null=True, blank=True)
    zoom_instructions = models.BooleanField(default=False)
    meeting_ID = models.CharField(max_length=15, null=True, blank=True)
    password = models.CharField(max_length=15, null=True, blank=True)
    include_vids = models.JSONField(default=list)
    slug = models.SlugField(max_length=SLUG_LENGTH, null=False, unique=True)

    @property
    def time(self):
        if self.time_from and self.time_to:
            return f"{self.time_from.strftime('%-H:%M')}–{self.time_to.strftime('%-H:%M')} uur"
        else:
            return ''

    @property
    def speakers(self):
        return self.talk_set.order_by('pk').values_list('speaker', flat=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            main_title = self.title.split(':')[0]
            self.slug = f"{self.date.strftime('%Y-%m-%d')}-{slugify(main_title)}"
            self.slug = self.slug[:self.SLUG_LENGTH]
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y')}: {self.title}"

    class Meta:
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['-date']),
        ]
        ordering = ['-date']
        verbose_name_plural = 'Symposia'


class Talk(models.Model):
    title = models.CharField(max_length=300)
    symposium = models.ForeignKey(Symposium, on_delete=models.CASCADE)
    speaker = models.CharField(max_length=200)
    abstract = models.TextField()
    personalia = models.TextField()
    video_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.speaker}: {self.title}"


class ProgramItem(models.Model):
    symposium = models.ForeignKey(Symposium, on_delete=models.CASCADE)
    time_from = models.TimeField()
    time_to = models.TimeField(null=True, blank=True)
    name = models.CharField(max_length=200)

    @property
    def time(self):
        if self.time_to:
            return f"{self.time_from.strftime('%-H:%M')}–{self.time_to.strftime('%-H:%M')}"
        else:
            return f"{self.time_from.strftime('%-H:%M')}"

    def __str__(self):
        return f"{self.time}: {self.name}"


class AdditionalInfo(models.Model):
    name = models.CharField(max_length=200, unique=True)
    content = models.TextField()
