from django.db import models

# Create your models here.

class Tweets(models.Model):
    id = models.AutoField('tweet ID', serialize=False, serialize=False, auto_created=True, primary_key=True)
    source = models.CharField('デバイス', )