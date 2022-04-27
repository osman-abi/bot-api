from typing import ChainMap
from django.db import models

# Create your models here.

class CallMeUsers(models.Model):
    name         = models.CharField(max_length=250, blank=True, null=True)
    surname      = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    page_source  = models.CharField(max_length=250, blank=True, null=True)
    status       = models.CharField(max_length=250, blank=True, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class WaitingListUsers(models.Model):
    name         = models.CharField(max_length=250, blank=True, null=True)
    surname      = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=250, blank=True, null=True)
    brand_name   = models.CharField(max_length=250, blank=True, null=True)
    # model_name   = models.CharField(max_length=250, blank=True, null=True)
    price_range  = models.CharField(max_length=250, blank=True, null=True)
    page_source  = models.CharField(max_length=250, blank=True, null=True)
    status       = models.CharField(max_length=250, blank=True, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class CarBuyerUsers(models.Model):
    name         = models.CharField(max_length=250, blank=True, null=True)
    surname      = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=250, blank=True, null=True)
    brand_name   = models.CharField(max_length=250, blank=True, null=True)
    model_name   = models.CharField(max_length=250, blank=True, null=True)
    price_range  = models.CharField(max_length=250, blank=True, null=True)
    link         = models.CharField(max_length=1000, blank=True, null=True)
    page_source  = models.CharField(max_length=250, blank=True, null=True)
    status       = models.CharField(max_length=250, blank=True, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"