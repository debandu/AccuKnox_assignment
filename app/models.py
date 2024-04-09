from django.db import models

# Create your models here.

class test(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    data=models.CharField(max_length=255)

class after_test(models.Model):
    test_id=models.OneToOneField(test, on_delete=models.CASCADE)
    number=models.IntegerField(null=False)
