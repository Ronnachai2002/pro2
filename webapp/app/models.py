from django.db import models
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images_profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    pass1 = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Item(models.Model):
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=500)
    description = models.TextField(max_length=255, default='No description')
    material = models.CharField(max_length=50, default='No description')
    price = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True, blank=True, null=True)

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images', null=True, blank=True)

class Cart(models.Model):
    cart = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Detailcart(models.Model):
    itemImages = models.ForeignKey(ItemImage, on_delete=models.CASCADE)
    carts = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=[('A0', 'A0'), ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4')])
    material = models.CharField(max_length=50, choices=[('Vinyl', 'ป้ายไวนิลธงญี่ปุ่น'), ('Acrylic', 'ป้ายไวนิลโครงไม้/โครงเหล็ก'), ('Metal', 'ป้ายกล่องไฟไวนิล'), ('Wood', 'สติกเกอร์อิงค์เจ็ท'), ('Foamboard', 'แคนวาสอิงค์เจ็ท')])
    message = models.TextField()
    attachment = models.FileField(upload_to='order_attachments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)