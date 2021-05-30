
from django.contrib.auth.models import User  #to connect this model to user
from django.db import models  
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
    created_at= models.DateTimeField(auto_now_add=True) #to knnow when the order was created
    paid_amount= models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True) #paid amount it will get from the stripe 
    stripe_token=models.CharField(max_length=100)# used to perform the purchase 

    class Meta:
        ordering =['-created_at',] #decending order 

    def __str__(self):
        return self.first_name 

        
    
class OrderItem(models.Model):
        order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
        #i was making a class inside that class i need to delete space before the class i mean it's a new class.
   
        product = models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=8,decimal_places=2)
        quantity=models.IntegerField(default=1)

        def __str__(self):
            return '%s' % self.id
