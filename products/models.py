from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120) #models.Field is used to map these to database
    description =models.TextField(blank=True,null=True)
    price =models.DecimalField(decimal_places=2,max_digits=500)
    # summary=models.TextField(blank=True,null=False)IF BOOTH ARE FALSE ITS REQUIRED TO BE FILLED
    # featured=models.BooleanField(default=False) #null=True  default=True

    def get_absolute_url(self):
        return reverse('products:product_detail_view', kwargs={"id": self.id})