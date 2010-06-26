from django.db import models

from customers.models import Customer
from stocks.models import Stock, Warehouse


class Quotation(models.Model):
    invoice_no = models.IntegerField() # Starts at 1
    date = models.DateField()
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max_length=255)
    stocks = models.ManyToManyField(Stock)
    quantity = models.IntegerField(default=0, blank=True)
    discount = models.FloatField(default=0, blank=True)
    #clerk_name = # Fk to User
