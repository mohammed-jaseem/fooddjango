from django.db import models

ADDRESS_TYPE_CHOICES = (
    ('home','home'),
    ('work','work'),
    ('other','other')
)

from users.models import User
from restaurant.models import Food,Restaurant

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "customer_customer"
        verbose_name = "customer"
        verbose_name_plural = "customers"
        ordering = ["-id"]

    def __str__(self):
        return self.user.email
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        db_table = "customer_cart"
        verbose_name = "cart"
        verbose_name_plural = "carts"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)
    

class CartBill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey('customer.Address', on_delete=models.SET_NULL, null=True, blank=True)
    item_totel = models.FloatField()
    offer_amount = models.FloatField()
    totel_amount = models.FloatField()
    delivery = models.IntegerField()

    class Meta:
        db_table = "customer_cartbill"
        verbose_name = "cartbill"
        verbose_name_plural = "cartbills"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)
    

class Offer(models.Model):
    code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    short_description = models.TextField() 
    is_percentage = models.BooleanField()

    class Meta:
        db_table = "customer_offer"
        verbose_name = "offer"
        verbose_name_plural = "offers"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)
    
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=225)
    appartment = models.CharField(max_length=225)
    landmark = models.CharField(max_length=225)
    address_type = models.CharField(max_length=255,choices=ADDRESS_TYPE_CHOICES)

    

    class Meta:
        db_table = "customer_address"
        verbose_name = "address"
        verbose_name_plural = "address"
        ordering = ["-id"]

    def __str__(self):
        return self.landmark
    
class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        db_table = "customer_order_item"
        verbose_name = "order_item"
        verbose_name_plural = "order_items"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_item = models.ManyToManyField(OrderItem)
    order_id = models.CharField(max_length=225)
    item_totel = models.FloatField()
    offer_amount = models.FloatField()
    totel_amount = models.FloatField()
    delivery = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    appartment = models.CharField(max_length=225)
    landmark = models.CharField(max_length=225)

    class Meta:
        db_table = "customer_order"
        verbose_name = "order"
        verbose_name_plural = "orders"
        ordering = ["-id"]

    def __str__(self):
        return self.landmark

    





