import cloudinary
from cloudinary.models import CloudinaryField

from django.db import models
from django.utils.safestring import mark_safe

from levensfilosofie.fields import CleanHTMLField


class Member(models.Model):
    prefix = models.CharField(
        'Prefix', max_length=20, blank=True, null=True,
        help_text="Bijv.: 'Prof. dr.'"
    )
    first_name = models.CharField(
        'Voornaam', max_length=20, blank=True, null=True
    )
    preposition = models.CharField(
        'Tussenvoegsel', max_length=20, blank=True, null=True
    )
    last_name = models.CharField('Achternaam', max_length=20)
    suffix = models.CharField(
        'Suffix', max_length=20, blank=True, null=True,
        help_text="Bijv.: 'MA'"
    )
    personalia = CleanHTMLField('Personalia')
    picture = CloudinaryField('Afbeelding', blank=True, null=True)

    def _yield_name_parts(self):
        for name_part in [
            self.prefix, self.first_name, self.preposition,
            self.last_name, self.suffix
        ]:
            if name_part:
                yield name_part

    @property
    def name(self):
        return ' '.join(name_part for name_part in self._yield_name_parts())

    def picture_preview(self):
        if self.picture:
            return mark_safe(
                self.picture.image(transformation=[{
                    'height': 150, 'width': 150, 'crop': 'thumb',
                    'gravity': 'face'
                }])
            )
        else:
            return ''

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lid"
        verbose_name_plural = "Leden"
