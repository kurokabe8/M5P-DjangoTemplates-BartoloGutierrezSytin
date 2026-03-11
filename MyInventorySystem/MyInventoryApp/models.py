from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField()

    def getName(self):
        return self.name
    
    def __str__(self):
        return f'{self.name} - {self.city}, {self.country} created at: {self.created_at}'

class WaterBottle(models.Model):
    sku = models.CharField(max_length=300, unique=True)
    brand = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=300)
    mouth_size = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_quantity = models.IntegerField()

    def __str__(self):
        return f'SKU: {self.sku}, {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplied_by.getName()}, {self.cost} : {self.current_quantity}'
