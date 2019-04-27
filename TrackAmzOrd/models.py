from django.db import models

class Order(models.Model):
    ord_date = models.DateField('order date')
    ord_url = models.CharField(max_length=500)
    ord_name = models.CharField(max_length=200)
    def __str__(self):
        return self.ord_name
