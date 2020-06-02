from django.db import models

from django.contrib.auth.models import User

class Provider(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'
    
class Consumer(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    adress = models.TextField(default='')
    geo_location = models.CharField(max_length=250, default='')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'

class Category(models.Model):
    name = models.CharField(max_length=250, default='')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class subcategory(models.Model):
    name = models.CharField(max_length=250, default='')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return '%s (%s)' % (self.name, self.category)
    
    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'
        
class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='product', null=True, blank=True)
    subcategory = models.ForeignKey(subcategory,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.subcategory)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    

class Store(models.Model):
    Provider = models.ForeignKey(Provider,on_delete=models.CASCADE, null=True, blank=True)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)
    price_TT = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_retail = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

class Order(models.Model):
    
    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finished', 'finished order'),
    )

    Consumer = models.ForeignKey(Consumer,on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=250, default='new', choices=STATUS)
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class OrderProduct(models.Model):

    Product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)
    Order = models.ForeignKey(Order,on_delete=models.CASCADE, null=True, blank=True)
    ammount = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'

