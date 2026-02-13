from django.db import models

# Create your models here.
class MerchantDatabase(models.Model):
    id=models.AutoField(primary_key=True)
    mname=models.CharField(max_length=255, null=False)
    mnumber=models.CharField(max_length=50, null=False, unique=True)
    memail=models.EmailField(unique=True, null=False)
