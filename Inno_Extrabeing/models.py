from email.policy import default
from django.db import models

class User_detail(models.Model):
     Name                = models.CharField(max_length=50, null=True)
     DOB                 = models.DateField(max_length=50,null=True)
     Email               = models.EmailField(null=True)
     Password            = models.CharField(max_length=120, null=True)
     Mobile_Number       = models.CharField(max_length=10, null=True)
     Gender              = models.CharField(max_length=20, null=True)
     Geo_Location        = models.CharField(max_length=120, null=True)
     Registered_at       = models.DateTimeField(auto_now_add=True, null=True)



class Store_detail(models.Model):
     Store_Name          = models.CharField(max_length=50,null=True)
     Email               = models.EmailField(null=True)
     Password            = models.CharField(max_length=120, null=True)
     Mobile_Number       = models.CharField(max_length=10, null=True)
     Geo_Location        = models.CharField(max_length=120, null=True)
     Registered_at       = models.DateTimeField(auto_now_add=True, null=True)



class Product_detail(models.Model):
     Store                 =models.ForeignKey(Store_detail,on_delete=models.CASCADE)
     Product_Name          =models.CharField(max_length=50)
     Product_Price         =models.IntegerField(null=True)
     Product_Description   =models.CharField(max_length=200, null=True)
     Registered_at         = models.DateTimeField(auto_now_add=True, null=True)


class Cart_detail(models.Model):
     User                  =models.ForeignKey(User_detail,on_delete=models.CASCADE)
     Detail                =models.TextField(null=True)


class User_Security(models.Model):
     User                  =models.ForeignKey(User_detail,on_delete=models.CASCADE)
     Email                 =models.EmailField(null=True)
     Token                 =models.CharField(max_length=30, null=True) 
     Generated_at          =models.DateTimeField(auto_now_add=True, null=True)

class Store_Security(models.Model):
     Store                 =models.ForeignKey(Store_detail,on_delete=models.CASCADE)
     Email                 =models.EmailField(null=True)
     Token                 =models.CharField(max_length=30, null=True)
     Generated_at          =models.DateTimeField(auto_now_add=True, null=True) 


class Order_detail(models.Model):
      User                  =models.ForeignKey(User_detail,on_delete=models.CASCADE)
      Store                 =models.ForeignKey(Store_detail,on_delete=models.CASCADE)
      Product               =models.ForeignKey(Product_detail,on_delete=models.CASCADE)            
      Quantity              =models.IntegerField(null=True)
      Order_Status          =models.CharField(max_length=10, default="Pending",null=False)
      Ordered_at            =models.DateTimeField(null=True)

