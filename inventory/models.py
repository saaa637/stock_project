from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit = models.CharField(max_length=20, default="pcs")
    total_stock = models.FloatField(default=0)

    def __str__(self):
        return self.name

class StockEntry(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.FloatField()
    type = models.CharField(
        max_length=10,
        choices=[("IN", "Stock In"), ("OUT", "Stock Out")]
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.material.name} - {self.type} - {self.quantity}"
