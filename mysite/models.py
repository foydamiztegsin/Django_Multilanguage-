from django.db import models

class Categories(models.Model):
    name                = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.name
    
    
class Products(models.Model):
    category_id         = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name        = models.CharField(max_length=250)
    product_price       = models.IntegerField()
    product_discription = models.TextField()
    
    def __str__(self) -> str:
        return self.product_name
