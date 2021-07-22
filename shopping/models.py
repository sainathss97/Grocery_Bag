from django.db import models
from django.contrib.auth.models import User

# Create your models here.
status = (('available','available'),('bought', 'bought'),('pending','pending'), ('not available','not available'))
class Cart_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank =True,null =True)
    item_name = models.CharField( max_length=100)
    item_quantity = models.IntegerField()
    item_status = models.CharField( max_length=20,choices = status,default = 'available')
    date = models.DateField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.item_name 

