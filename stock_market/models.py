
from django.db import models



class Data(models.Model):
    date=models.DateField()
    trade_code=models.CharField(max_length=150)
    high=models.FloatField(max_length=15)
    low=models.FloatField(max_length=15)
    open=models.FloatField(max_length=15)
    close=models.FloatField(max_length=15)
    volume=models.IntegerField(max_length=15)
