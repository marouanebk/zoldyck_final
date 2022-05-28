import datetime
from statistics import mode
from django.db import models
from accounts.models import Account


# Create your models here.
class Notification(models.Model):

    to_user = models.ForeignKey(Account, related_name='notification_to', on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(Account, related_name='notification_from', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    user_has_seen = models.BooleanField(default=False)
    reminder = models.BooleanField(default=False)
