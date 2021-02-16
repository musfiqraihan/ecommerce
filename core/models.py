from django.db import models
from django.conf import settings


class ItemList(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title
    

class OrderItemList(models.Model):
    item = models.ForeignKey(ItemList, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.title


class OrderList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItemList)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()


    def __str__(self):
        return self.title


