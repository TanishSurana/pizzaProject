from django.db import models
from django.core.exceptions import ValidationError 
from django.contrib.auth.models import User
  

def is_positive(value):
    if value >= 0:
        return value
    else: 
        raise ValidationError("should be a positive value")









# Create your models here.

class Topping(models.Model):
    toppingname = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.toppingname}"

class Regularpizza(models.Model):
    itemname = models.CharField(max_length=64, unique=True)
    smallcost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    largecost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    ntoppings = models.IntegerField(default = 0, validators =[is_positive])
    extrasEnable = models.BooleanField(default=False)
    sizeEnable = models.BooleanField(default=True)
    # toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
       return f"{self.itemname}: small:{self.smallcost}, large:{self.largecost}, no.toppings:{self.ntoppings}"

class Sicilianpizza(models.Model):
    itemname = models.CharField(max_length=64, unique=True)
    smallcost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    largecost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    ntoppings = models.IntegerField(default = 0, validators =[is_positive])
    extrasEnable = models.BooleanField(default=False)
    sizeEnable = models.BooleanField(default=True)
    # toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f"{self.itemname}: small:{self.smallcost}, large:{self.largecost}, no.toppings:{self.ntoppings}"



class Extra(models.Model):
    itemname = models.CharField(max_length=64, unique=True)
    smallcost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    largecost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])


class Pasta(models.Model):
    itemname = models.CharField(max_length=64, unique=True)
    smallcost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    extrasEnable = models.BooleanField(default=False)
    sizeEnable = models.BooleanField(default=False)
    ntoppings = models.IntegerField(default = 0, validators =[is_positive])

    def __str__(self):
        return f"{self.itemname} - ${self.smallcost}"

class Salad(models.Model):
    itemname = models.CharField(max_length=64, unique=True)
    smallcost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    ntoppings = models.IntegerField(default = 0, validators =[is_positive])
    extrasEnable = models.BooleanField(default=False)
    sizeEnable = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.itemname} - ${self.smallcost}"

class Subs(models.Model):
    itemname = models.CharField(max_length=64, unique=True)
    smallcost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive], blank=True,null=True)
    largecost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    extrasEnable = models.BooleanField(default=True)
    ntoppings = models.IntegerField(default = 0, validators =[is_positive])
    sizeEnable = models.BooleanField(default=True)
    # extras = models.ManyToManyField(Extra, blank=True)

    def __str__(self):
        return f"{self.itemname}: small:{self.smallcost}, large:{self.largecost}, extras={self.extrasEnable}"


class Dinnerplatter(models.Model):
    itemname = models.CharField(max_length=64, unique=True)
    smallcost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    largecost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    ntoppings = models.IntegerField(default = 0, validators =[is_positive])
    extrasEnable = models.BooleanField(default=False)
    sizeEnable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.itemname}: small:{self.smallcost}, large:{self.largecost}"

class Menuitem(models.Model):
    itemname = models.CharField(max_length=64)
    cat = models.CharField(max_length=64)
    toppings = models.ManyToManyField(Topping, blank=True)
    extras = models.ManyToManyField(Extra, blank=True)
    cost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])

class Order(models.Model):
    items = models.ManyToManyField(Menuitem, null=True ,blank=True)
    cost = models.DecimalField(max_digits=5,decimal_places=2, validators =[is_positive])
    status = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    