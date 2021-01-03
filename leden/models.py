from django.db import models

class Member(models.Model):
    key = models.CharField(max_length=5, primary_key=True)
    prefix = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=20, null=True)
    preposition = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    suffix = models.CharField(max_length=20, null=True)
    personalia = models.TextField(null=True)

    def name(self):
        return ' '.join(
            name_part for name_part in
            [self.prefix, self.first_name, self.preposition, self.last_name, self.suffix]
            if name_part
        )
