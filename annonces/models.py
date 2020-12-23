from django.db import models
from django.template.defaultfilters import slugify


class Symposium(models.Model):
    title = models.CharField(max_length=300, unique=True)
    introduction = models.TextField(null=True)
    date = models.DateField(unique=True)
    time = models.CharField(max_length=50, null=True)
    place = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=False, unique=True)

    def speakers(self):
        return Talk.objects.filter(symposium=self).order_by('number').values_list('speaker', flat=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Talk(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=300)
    symposium = models.ForeignKey(Symposium, on_delete=models.CASCADE)
    speaker = models.CharField(max_length=200)
    abstract = models.TextField()
    personalia = models.TextField()

    def __str__(self):
        return f"{self.speaker}: {self.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['number', 'symposium'], name='unique_talk_ordering')
        ]


class ProgramItem(models.Model):
    number = models.IntegerField()
    symposium = models.ForeignKey(Symposium, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.time}: {self.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['number', 'symposium'], name='unique_program_ordering')
        ]
