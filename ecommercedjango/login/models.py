from django.db import models

# Create your models here.
class EcommerceDatabase(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255, null=False)
    number=models.CharField(max_length=255, null=False, unique=True)
    email=models.EmailField(max_length=255, null=False, unique=True)
    password=models.CharField(max_length=255, null=False, unique=True)