from datetime import datetime

from django.db import models

from geography.models import City, Country
from utils.constants import PRICE_CHOICES


class Customer(models.Model):
    cutomer_no = models.CharField(max_length=100)  # LLL-FFF-N, 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True)
    price_type = models.CharField(max_length=2, choices=PRICE_CHOICES)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    home_phone = models.CharField(max_length=50, blank=True)
    work_phone = models.CharField(max_length=50, blank=True)
    cell_phone = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    vat_flag = models.BooleanField(default=False)
    vat_registration_number = models.IntegerField(default=0, blank=True)  # 8 digit max
    business_registration_number = models.CharField(max_length=9, blank=True)
    discount_percent = models.FloatField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now())

    class Meta:
        unique_together = (('first_name', 'last_name'),)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
