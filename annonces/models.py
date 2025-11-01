from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError

from annonces.unsplash import get_unsplash_data
from levensfilosofie.fields import CleanHTMLField, CleanHTMLLineField

from requests import HTTPError


class Symposium(models.Model):
    SLUG_LENGTH = 200

    title = models.CharField("Titel", max_length=300)
    subtitle = models.CharField("Ondertitel", max_length=300, null=True, blank=True)
    introduction = CleanHTMLField("Introductie", null=True, blank=True)
    date = models.DateField("Datum", unique=True)
    time_from = models.TimeField("Begintijd", null=True, blank=True)
    time_to = models.TimeField("Eindtijd", null=True, blank=True)
    place = models.CharField("Locatie", max_length=200, null=True, blank=True)
    entrance = models.CharField(
        "Toegang",
        max_length=10,
        choices=[
            ("voluntary", "Vrijwillige bijdrage"),
            ("free", "Vrij"),
        ],
        default="voluntary",
    )
    photo_id = models.CharField(
        "Omslagfoto (Unsplash ID)",
        max_length=200,
        null=True,
        blank=True,
        help_text=mark_safe(
            'Zie de <a href="https://unsplash.com/documentation">API documentatie</a>.'
        ),
    )
    photo = models.JSONField(default=dict)
    zoom_link = models.CharField(
        "Zoom Link",
        max_length=100,
        blank=True,
        null=True,
    )
    extra_announcement = models.CharField(
        "Extra mededeling", max_length=200, null=True, blank=True
    )
    to_be_announced = models.BooleanField(
        "Nog aan te kondigen",
        default=False,
        help_text=(
            "Vink aan als de informatie nog niet volledig is. Het symposium "
            "zal in de agenda verschijnen op de homepage, maar krijgt nog "
            "niet een aparte pagina."
        ),
    )
    include_vids = models.JSONField(default=list)
    slug = models.SlugField(max_length=SLUG_LENGTH, null=False, unique=True)
    canceled = models.BooleanField("Afgelast", default=False)
    canceled_message = CleanHTMLField(
        "Bericht bij het afgelasten",
        blank=True,
        help_text=(
            "Zal verschijnen op de pagina van de annonce en op de "
            "startpagina, wanneer daar normaliter ook een aankondiging zou "
            "verschijnen."
        ),
    )

    @property
    def full_title(self):
        return f"{self.title}: {self.subtitle}" if self.subtitle else self.title

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
            self.slug = f"{self.date.strftime('%Y-%m-%d')}-{slugify(self.title)}"
            self.slug = self.slug[: self.SLUG_LENGTH]

        return super().save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        if self.photo_id:
            try:
                self.photo = get_unsplash_data(self.photo_id)
            except HTTPError as e:
                raise ValidationError(
                    f"An error occured on Unsplash data request: {e} (ID: {self.photo_id})"
                )
        else:
            self.photo = {}
        return super().clean(*args, **kwargs)

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y')}: {self.full_title}"

    class Meta:
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["-date"]),
        ]
        ordering = ["-date"]
        verbose_name = "Symposium"
        verbose_name_plural = "Symposia"


class Talk(models.Model):
    title = models.CharField("Titel", max_length=300, null=True, blank=True)
    symposium = models.ForeignKey(Symposium, on_delete=models.CASCADE)
    speaker = models.CharField("Spreker", max_length=200)
    abstract = CleanHTMLField("Abstract", null=True, blank=True)
    personalia = CleanHTMLField("Personalia", null=True, blank=True)
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
    time_from = models.TimeField("Begintijd", null=True, blank=True)
    time_to = models.TimeField("Eindtijd", null=True, blank=True)
    name = CleanHTMLLineField("Naam")

    @property
    def time(self):
        if self.time_from and self.time_to:
            return (
                f"{self.time_from.strftime('%-H:%M')}–{self.time_to.strftime('%-H:%M')}"
            )
        elif self.time_from:
            return f"{self.time_from.strftime('%-H:%M')}"
        else:
            return ""

    def __str__(self):
        if self.time:
            return f"{self.time}: {self.name}"
        else:
            return self.name

    class Meta:
        verbose_name = "Programma-item"
        verbose_name_plural = "Programma-items"
