from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe

from levensfilosofie.fields import CleanHTMLField, CleanHTMLLineField


class Symposium(models.Model):

    SLUG_LENGTH = 200

    title = models.CharField("Titel", max_length=300)
    introduction = CleanHTMLField("Introductie", null=True, blank=True)
    date = models.DateField("Datum", unique=True)
    time_from = models.TimeField("Begintijd", null=True, blank=True)
    time_to = models.TimeField("Eindtijd", null=True, blank=True)
    place = models.CharField("Locatie", max_length=200, null=True, blank=True)
    zoom_link = models.CharField(
        "Zoom Link",
        max_length=100,
        blank=True,
        null=True,
        help_text=(
            "Uit veiligheidsoverwegingen verschijnt de zoomlink pas 3 dagen "
            "voor het symposium begint op de website, en hij verdwijnt daarna "
            "ook weer automatisch."
        ),
    )
    include_vids = models.JSONField(default=list)
    slug = models.SlugField(max_length=SLUG_LENGTH, null=False, unique=True)

    @property
    def time(self):
        if self.time_from:
            time_from = self.time_from.strftime("%-H:%M")
        else:
            return ""

        if self.time_to:
            return f"{time_from}–{self.time_to.strftime('%-H:%M')} uur"
        else:
            return f"{time_from} uur"

    @property
    def speakers(self):
        return self.talk_set.order_by("pk").values_list("speaker", flat=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            main_title = self.title.split(":")[0]
            self.slug = (
                f"{self.date.strftime('%Y-%m-%d')}-{slugify(main_title)}"
            )
            self.slug = self.slug[: self.SLUG_LENGTH]
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y')}: {self.title}"

    class Meta:
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["-date"]),
        ]
        ordering = ["-date"]
        verbose_name = "Symposium"
        verbose_name_plural = "Symposia"


class Talk(models.Model):
    title = models.CharField("Titel", max_length=300)
    symposium = models.ForeignKey(Symposium, on_delete=models.CASCADE)
    speaker = models.CharField("Spreker", max_length=200)
    abstract = CleanHTMLField("Abstract")
    personalia = CleanHTMLField("Personalia")
    video_id = models.CharField(
        "YouTube video ID",
        max_length=20,
        null=True,
        blank=True,
        help_text=mark_safe(
            'De ID is het deel van de YouTube URL direct na "v=", altijd 11 '
            "karakters lang. Bijvoorbeeld: "
            "https://www.youtube.com/watch?v=<b>dQw4w9WgXcQ</b>"
        ),
    )

    def __str__(self):
        return f"{self.speaker}: {self.title}"

    class Meta:
        verbose_name = "Lezing"
        verbose_name_plural = "Lezingen"


class ProgramItem(models.Model):
    symposium = models.ForeignKey(Symposium, on_delete=models.CASCADE)
    time_from = models.TimeField("Begintijd")
    time_to = models.TimeField("Eindtijd", null=True, blank=True)
    name = CleanHTMLLineField("Naam")

    @property
    def time(self):
        if self.time_to:
            return f"{self.time_from.strftime('%-H:%M')}–{self.time_to.strftime('%-H:%M')}"
        else:
            return f"{self.time_from.strftime('%-H:%M')}"

    def __str__(self):
        return f"{self.time}: {self.name}"

    class Meta:
        verbose_name = "Programma-item"
        verbose_name_plural = "Programma-items"
