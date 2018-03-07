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
    preference = models.CharField(max_length=200, blank=True, default="")


class LabelUser(ListenerUser):
    """ Label Participant """
    label_info = models.CharField(max_length=200, blank=True, default="")


class TrackLabel(models.Model):
    owner = models.ForeignKey(User, related_name="track_labels", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
