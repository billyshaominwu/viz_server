from django.db import models
import uuid
# Create your models here.

class Crime(models.Model):
    __tablename__ = 'crimes'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.IntegerField(primary_key=True)
    offense_type = models.CharField(max_length=200)
    offense_description = models.CharField(max_length=200)
    report_date = models.DateTimeField(null=True)
    offense_start_date = models.DateTimeField(null=True)
    offense_end_date = models.DateTimeField(null=True)
    block = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    beat = models.CharField(max_length=200)
    census_tract = models.CharField(max_length=200)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    # time = models.DateTimeField()