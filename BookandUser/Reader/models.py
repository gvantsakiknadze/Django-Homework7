from django.db import models

# Create your models here.
class Reader(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    age = models.IntegerField()
    GENDER_CHOICES = (
        (0,'male'),
        (1,'female'),
        (2, 'not specified'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)