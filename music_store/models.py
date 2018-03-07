from django.db import models


class DefaultUser(models.Model):
    email = models.CharField(max_length=100, default='', editable=False)
    password = models.CharField(max_length=100, default='')

    name = models.CharField(max_length=100, blank=True, default='')
    is_active = models.BooleanField(default=False)


class ListenerUser(DefaultUser):
    created = models.DateTimeField(auto_now_add=True)
