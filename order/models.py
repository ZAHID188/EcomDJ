from django.db import models
from django.contrib.auth.models import User  #to connect this model to user
from product.models import Product # bring product here


class Order(models.Model):
    user = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100) 
    place=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    paid_amount= models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    stripe_token=models.CharField(max_length=100)

    class Meta:
        ordering=['-created_at',] #decending order 

    def __str__(self):
        return self.first_name 

        
    
class OrderItem(models.Model):
        order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)#here is an error should be 'Order'=Order
        # but if i use Order then it's having a name error
   
        product = models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=8,decimal_places=2)
        quantity=models.IntegerField(default=1)

        def __str__(self):
            return '%s' % self.id
