from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class YelpBusinessItem(models.Model):
    url = models.URLField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now())


class Review(models.Model):
    page = models.ForeignKey(YelpBusinessItem, on_delete=models.CASCADE)
    rating = models.CharField(max_length=7)
    comment = models.TextField()
    date = models.DateTimeField()
    reviewer = models.TextField()
    reviewer_address = models.TextField()
    date_created = models.DateTimeField(default=datetime.now())
