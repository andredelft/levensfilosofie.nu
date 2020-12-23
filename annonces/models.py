from django.db import models


class Symposium(models.Model):
    title = models.CharField(max_length=300)
    introduction = models.TextField(null=True)
    date = models.DateField()
    time = models.CharField(max_length=50, null=True)
    place = models.CharField(max_length=200, null=True)

    def speakers(self):
        return Talk.objects.filter(symposium=self).values_list('speaker', flat=True)

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
