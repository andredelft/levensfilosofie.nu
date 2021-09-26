from django.db import models
from django.template.defaultfilters import slugify

from .fields import CleanHTMLField, CleanHTMLLineField


class Symposium(models.Model):

    SLUG_LENGTH = 200

    title = CleanHTMLLineField('Titel')
    introduction = CleanHTMLField('Introductie', null=True, blank=True)
    date = models.DateField('Datum', unique=True)
    time_from = models.TimeField('Begintijd', null=True, blank=True)
    time_to = models.TimeField('Eindtijd', null=True, blank=True)
    place = models.CharField('Locatie', max_length=200, null=True, blank=True)
    zoom_instructions = models.BooleanField('Zoom instructies', default=False)
    meeting_ID = models.CharField('Meeting ID', max_length=15, null=True, blank=True)
    password = models.CharField('Wachtwoord', max_length=15, null=True, blank=True)
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
        verbose_name = 'Symposium'
        verbose_name_plural = 'Symposia'


class Talk(models.Model):
    title = CleanHTMLLineField('Titel')
    symposium = models.ForeignKey(Symposium, on_delete=models.CASCADE)
    speaker = models.CharField('Spreker', max_length=200)
    abstract = CleanHTMLField('Abstract')
    personalia = CleanHTMLField('Personalia')
    video_id = models.CharField('Video ID', max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.speaker}: {self.title}"

    class Meta:
        verbose_name = 'Lezing'
        verbose_name_plural = 'Lezingen'


class ProgramItem(models.Model):
    symposium = models.ForeignKey(Symposium, on_delete=models.CASCADE)
    time_from = models.TimeField('Begintijd')
    time_to = models.TimeField('Eindtijd', null=True, blank=True)
    name = CleanHTMLLineField('Naam')

    @property
    def time(self):
        if self.time_to:
            return f"{self.time_from.strftime('%-H:%M')}–{self.time_to.strftime('%-H:%M')}"
        else:
            return f"{self.time_from.strftime('%-H:%M')}"

    def __str__(self):
        return f"{self.time}: {self.name}"

    class Meta:
        verbose_name = 'Programma-item'
        verbose_name_plural = 'Programma-items'


class AdditionalInfo(models.Model):
    name = models.CharField(max_length=200, unique=True)
    content = CleanHTMLField()
