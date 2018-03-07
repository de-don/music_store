from django.db import models
from django.contrib.auth.models import User


class DefaultUser(User):
    """ default user model

    Attrs:
        balance: added just for test
    """

    balance = models.FloatField(default=0.0)


class ListenerUser(DefaultUser):
    """ Simple listener """
    preference = models.CharField(max_length=200, blank=True)


class LabelUser(DefaultUser):
    """ Label Participant """
    label_info = models.CharField(max_length=200, blank=True)
