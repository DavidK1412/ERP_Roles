from django.db import models


class Module(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    permissions = models.ManyToManyField('Permission', related_name='modules')

    def __str__(self):
        return self.name
