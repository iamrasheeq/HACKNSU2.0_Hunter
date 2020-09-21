from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=11, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
	name = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=11, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ForeignKey(Tag, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name

class Product(models.Model):



    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    buy_Price = models.IntegerField(null=True)
    sell_Price = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ForeignKey(Tag, null=True, on_delete = models.SET_NULL)
    def __str__(self):
        return self.name

class Product_Request(models.Model):


    product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    quantity = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ForeignKey(Tag, null=True, on_delete = models.SET_NULL)

    def __str__(self):
	       return self.product.name

class Client_Order(models.Model):

    STATUS =(
    ('Complete','Complete'),('Pending','Pending'),('Out for delivery','Out for delivery'),
    )

    client = models.ForeignKey(Client, null=True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    quantity = models.IntegerField(null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
	       return self.product.name
    # def __str__(self):
    #     return self.product

class Vendor_Order(models.Model):

    STATUS =(
    ('Complete','Complete'),('Pending','Pending'),
    )

    product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    vendor = models.ForeignKey(Vendor, null=True, on_delete = models.SET_NULL)
    quantity = models.IntegerField(null=True)

    status = models.CharField(max_length=50, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
	       return self.product.name

    # def __str__(self):
    #     return self.product
