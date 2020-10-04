from django.db import models
from datetime import datetime
from datetime import timezone
class Resource(models.Model):

    unique_identifier = models.CharField(max_length=100, null = True)
    name = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=50, default=str(datetime.now().replace(tzinfo=timezone.utc).timestamp()))
    