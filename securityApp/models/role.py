from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=255)
    description = models.CharField('Description', max_length=255)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)
    permissions = models.ManyToManyField('securityApp.Permission', related_name='roles')
