import string
from django.shortcuts import render,get_object_or_404
import json
import random
import datetime
from django.http  import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User_Security, User_detail, Product_detail, Store_detail,Cart_detail,Store_Security,Order_detail
import re


def User_registration_view(request):
    if request.method == 'POST':

         data = json.loads(request.body)
         Name_r               = data['Name']
         DOB_r                = data['DOB']
         Email_r              = data['Email']
         Password_r           = data['Password']
         C_Password_r         = data['C_Password']
         Mobile_Number_r      = data['Mobile_Number']
         Gender_r             = data['Gender']
         Geo_Location_r       = data['Geo_Location']
         
         
         email_condition = "^[a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}$"
         match = re.search(email_condition,Email_r)
         
         if (not Name_r):
             mes = {
             'message': 'Name Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Email_r):
             mes = {   
             'message': 'Email Required!'
             }
             return JsonResponse(mes,status=403,safe=False)    
         if (not match):
             mes = {    
             'message': 'Invalid Email!'
             }
             return JsonResponse(mes,status=403,safe=False)

         if (User_detail.objects.filter(Email = Email_r)):
             mes = {  
             'message': 'Email Already Exists!'
             }
             return JsonResponse(mes,status=403,safe=False)    
             
         if (not Mobile_Number_r):
             mes = {   
             'message': 'Mobile Number Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (len(Mobile_Number_r) != 10):
             mes = {   
             'message': 'Invalid Mobile Number!'
             }
             return JsonResponse(mes,status=403,safe=False)    
         if (not DOB_r):
             mes = {  
              'message': 'DOB Required!'
             }
             return JsonResponse(mes,status=403,safe=False)       
                
         if (not Password_r):
             mes = {    
             'message': 'Password Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not C_Password_r):
             mes = {   
             'message': 'Confirm Password Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
             
         if (not Gender_r):
             mes = {    
             'message': 'Gender Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
        
         if (Geo_Location_r == "Click to Get Location"):
             mes = {     
             'message': 'Geo Location Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
                               
         if (Password_r != C_Password_r):
             mes = { 
             'message': 'Password do not Match!'
             }
             return JsonResponse(mes,status=403,safe=False) 
             
         else:
          Password_h = make_password(Password_r)
          new_user = User_detail(Name=Name_r, DOB=DOB_r, Email=Email_r, Password=Password_h,Mobile_Number=Mobile_Number_r, Gender=Gender_r, Geo_Location=Geo_Location_r)
          new_user.save()
          mes = {
          'message': 'User Created Successfully!'
           }
          return JsonResponse(mes,status=200,safe=False)



def User_login_view(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        Email_l = data['Email']
        Password_l = data['Password']
        if (User_detail.objects.filter(Email = Email_l).exists()):
                User_list    = User_detail.objects.filter(Email = Email_l)[0]
                Password_c   = User_list.Password
                Password_cr  = check_password(Password_l , Password_c)
                a=list((string.ascii_letters+string.digits+"!@#$%^&*"))
                s=""
                for i in range(20):
                 b=random.choice(a)
                 s+=b
                x=User_detail.objects.get(Email=data['Email'])
                
                if Password_cr:
                    Security = User_Security(User=x,Email=Email_l,Token=s)
                    Security.save()
                    mes = {  
                    'message'        :'Login Successful!',
                    'Token'          :s
                    }
                    return JsonResponse(mes,status=200,safe=False)
                    
                else:
                    mes = {
                    'message':'Wrong Password!'
                    }
                    return JsonResponse(mes,status=403,safe=False)
        
        else:
             
             mes = {
             'message':'Invalid User!'
                   }
             return JsonResponse(mes,status=403,safe=False)



def User_dash(request):
        if request.method == 'POST':
        
           data = json.loads(request.body)     
           Token_d = data['Token']
           Key_d   = data['Key']
           if (Key_d == 69):  
             if (User_Security.objects.filter(Token = Token_d).exists()):
               User_s       =User_Security.objects.filter(Token = Token_d)[0]
               Email_d      = User_s.Email
               User_li      = User_detail.objects.filter(Email = Email_d)
               User_det     = list(User_li.values('Name','DOB','Email','Mobile_Number','Gender','Geo_Location'))[0]

               Store_li      = Store_detail.objects.all()
               Store_det     = list(Store_li.values('id','Store_Name','Email','Mobile_Number','Geo_Location'))
               
               mes = {      
                    'User_detail'    :User_det,
                    'Store_detail'   :Store_det
                    }
               return JsonResponse(mes,status=200,safe=False)
             else:   
               mes = {
                        'message':'Invalid User!'
                     }
               return JsonResponse(mes,status=403,safe=False)



def User_Logout(request):
    if request.method == 'POST':
        data = json.loads(request.body)     
        Token_d = data['Token']               
        Security = User_Security.objects.get(Token=Token_d)
        Security.delete()
        mes = {      
        'message'    :"Token Deleted!"
        }
        return JsonResponse(mes,status=200,safe=False)





def Store_registration_view(request):
    if request.method == 'POST':

         data = json.loads(request.body)
         Store_Name_r         = data['Store_Name']
         Email_r              = data['Email']
         Password_r           = data['Password']
         C_Password_r         = data['C_Password']
         Mobile_Number_r      = data['Mobile_Number']
         Geo_Location_r       = data['Geo_Location']
         
         email_condition = "^[a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}$"
         match = re.search(email_condition,Email_r)
         
         if (not Store_Name_r):
             mes = {
             'message': 'Store Name Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (Store_detail.objects.filter(Store_Name = Store_Name_r)):
             mes = {  
             'message': 'Store Name Already Exists!'
             }
             return JsonResponse(mes,status=403,safe=False)    
         if (not Email_r):
             mes = {   
             'message': 'Email Required!'
             }
             return JsonResponse(mes,status=403,safe=False)    
         if (not match):
             mes = {    
             'message': 'Invalid Email!'
             }
             return JsonResponse(mes,status=403,safe=False)   
         if (Store_detail.objects.filter(Email = Email_r)):
             mes = {  
             'message': 'Email Already Exists!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (len(Mobile_Number_r) != 10):
             mes = {   
             'message': 'Invalid Mobile Number!'
             }
             return JsonResponse(mes,status=403,safe=False)       
         if (not Mobile_Number_r):
             mes = {   
             'message': 'Mobile Number Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (len(Mobile_Number_r) != 10):
             mes = {   
             'message': 'Invalid Mobile Number!'
             }
             return JsonResponse(mes,status=403,safe=False)
         
         if (not Password_r):
             mes = {    
             'message': 'Password Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not C_Password_r):
             mes = {   
             'message': 'Confirm Password Required!'
             }
             return JsonResponse(mes,status=403,safe=False)
             
         if (Geo_Location_r == "Click to Get Location"):
             mes = {     
             'message': 'Geo Location Required!'
             }
             return JsonResponse(mes,status=403,safe=False)                       

         if (Password_r != C_Password_r):
             mes = { 
             'message': 'Password do not Match!'
             }
             return JsonResponse(mes,status=403,safe=False) 
             
         else:
          Password_h = make_password(Password_r)
          new_Store = Store_detail(Store_Name=Store_Name_r, Email=Email_r, Password=Password_h,Mobile_Number=Mobile_Number_r, Geo_Location=Geo_Location_r)
          new_Store.save()
          mes = {
          'message': 'Store Created Successfully!'
           }
          return JsonResponse(mes,status=200,safe=False)



def Store_login_view(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        Email_l = data['Email']
        Password_l = data['Password']
        if (Store_detail.objects.filter(Email = Email_l).exists()):
                Store_list    = Store_detail.objects.filter(Email = Email_l)[0]
                Password_c   = Store_list.Password
                Password_cr  = check_password(Password_l , Password_c)
                a=list((string.ascii_letters+string.digits+"!@#$%^&*"))
                s=""
                for i in range(20):
                 b=random.choice(a)
                 s+=b
                x=Store_detail.objects.get(Email=data['Email'])

                if Password_cr:
                    Security = Store_Security(Store=x,Email=Email_l,Token=s)
                    Security.save()
                    mes = {  
                    'message'        :'Login Successful!',
                    'Token'          :s
                    }
                    return JsonResponse(mes,status=200,safe=False)
                    
                else:
                    mes = {
                    'message':'Wrong Password!'
                    }
                    return JsonResponse(mes,status=403,safe=False)


        else:
             
             mes = {
             'message':'Invalid Store!'
                   }
             return JsonResponse(mes,status=403,safe=False)



def Store_dash(request):
    if request.method == 'POST':
        
           data = json.loads(request.body)
           Key_d   = data['Key']     
           Token_d = data['Token']
            
           if (Key_d == 69):

            if (Store_Security.objects.filter(Token = Token_d).exists()):

               Store_s       =Store_Security.objects.filter(Token = Token_d)[0]
               Email_d      = Store_s.Email 
               Store_list    = Store_detail.objects.filter(Email = Email_d)[0]
               Store_li      = Store_detail.objects.filter(Email = Email_d)
               Store_det     = list(Store_li.values('Store_Name','Email','Mobile_Number','Geo_Location'))[0]


               if(Product_detail.objects.filter(Store = Store_list).exists()):
                   Product_li      = Product_detail.objects.filter(Store = Store_list)
                   Product_det     = list(Product_li.values('id','Product_Name','Product_Price','Product_Description'))
                   mes = {   
                    'Store_detail' :Store_det,   
                    'Product_detail' :Product_det
                    }
                   return JsonResponse(mes,status=200,safe=False)
               else:
                   mes = { 

                    'message' :'No Product Available!'
                    }
                   return JsonResponse(mes,status=403,safe=False)
            else:
                   mes = { 

                    'message' :'No Store Found!'
                    }
                   return JsonResponse(mes,status=403,safe=False)



def Store_Logout(request):
    if request.method == 'POST':
        data = json.loads(request.body)     
        Token_d = data['Token']               
        Security = Store_Security.objects.get(Token=Token_d)
        Security.delete()
        mes = {      
        'message'    :"Token Deleted!"
        }
        return JsonResponse(mes,status=200,safe=False)                   


                   


def Product_registration_view(request):
    if request.method == 'POST':

         data = json.loads(request.body)
         Product_Name_r          = data['Product_Name']
         Product_Price_r         = data['Product_Price']
        #  Product_Image_r         = data['Product_Image']
         Product_Description_r   = data['Product_Description']

         Key_d         = data['Key']
         Token_d       = data['Token']
         if (Key_d == 69):

            if (Store_Security.objects.filter(Token = Token_d).exists()):
               Store_l      =Store_Security.objects.filter(Token = Token_d)[0] 
               Email_d      = Store_l.Email
               Store_list    = Store_detail.objects.filter(Email = Email_d)[0]  
               if (not Product_Name_r):
                  mes = {
                  'message': 'Product Name Required!'
                  }
                  return JsonResponse(mes,status=403,safe=False)
               if (Product_detail.objects.filter(Product_Name = Product_Name_r , Store = Store_list )):
                  mes = {  
                  'message': 'Product already Exists!' 
                  }
                  return JsonResponse(mes,status=403,safe=False)
               if (not Product_Price_r):
                  mes = {
                  'message': 'Product Price Required!'
                  }
                  return JsonResponse(mes,status=403,safe=False)
            #    if (not Product_Image_r):
            #       mes = {
            #       'message': 'Product Image Required!'
            #       }
            #       return JsonResponse(mes,status=403,safe=False)   
               if (not Product_Description_r):
                  mes = {
                  'message': 'Product Description Required!'
                  }
                  return JsonResponse(mes,status=403,safe=False)    


               else:
                  new_Product = Product_detail(Store=Store_list, Product_Name=Product_Name_r, Product_Price=Product_Price_r,Product_Description=Product_Description_r)
                  new_Product.save()
                  mes = {
                  'message': 'Product Created Successfully!'
                 }
                  return JsonResponse(mes,status=200,safe=False)



def Product_dash(request):
    if request.method == 'POST':
        
           data = json.loads(request.body)     
           Email_d = data['Email']
           Key_d   = data['Key']
           if (Key_d == 69):

            if (Store_detail.objects.filter(Email = Email_d).exists()):

               Store_list    = Store_detail.objects.filter(Email = Email_d)[0]

  
               if(Product_detail.objects.filter(Store = Store_list).exists()):
                   Product_li      = Product_detail.objects.filter(Store = Store_list)
                   Product_det     = list(Product_li.values('id','Store','Product_Name','Product_Price','Product_Description'))
                   mes = {    
                    'Product_detail' :Product_det
                    }
                   return JsonResponse(mes,status=200,safe=False)
               else:
                   mes = { 

                    'message' :'No Product Available!'
                    }
                   return JsonResponse(mes,status=403,safe=False)     
           




def Cart_View(request):
        if request.method == 'POST':
        
           data = json.loads(request.body)
           Token_d       = data['Token']
           User_r        = data['User']     
           Detail_r      = data['Detail']
           
           if (User_Security.objects.filter(Token = Token_d).exists()):
               
                if (not User_r):
                      mes = {
                        'message': 'User Id Required!!'
                         }
                      return JsonResponse(mes,status=403,safe=False)

                if (not Detail_r):
                      mes = {
                        'message': 'Cart Detail Required!!'
                         }
                      return JsonResponse(mes,status=403,safe=False)


                else:
                   x=User_detail.objects.get(id=data['User'])   
                   Cart_data = Cart_detail(User=x,Detail=Detail_r)
                   Cart_data.save()
                   mes = {
                      'message': 'Cart Detail Saved Successfully!'
                         }
                   return JsonResponse(mes,status=200,safe=False)
            
           else:
                   mes = { 
                        'message' :'No User Found!'
                    }
                   return JsonResponse(mes,status=403,safe=False)      





def Order_View(request):
    if request.method == 'POST':
           data = json.loads(request.body)
           Token_d        = data['Token']
           Orders_r       = data['Orders']

           x = datetime.datetime.now()

           if (User_Security.objects.filter(Token = Token_d).exists()):
                User_s = User_Security.objects.filter(Token = Token_d)[0]
                Email_d = User_s.Email
                User_det =  User_detail.objects.filter(Email = Email_d)[0]
                
                
                    
                for i in  Orders_r:
                     Store_i        = i['Store']
                     Product_i      = i['Product']  
                     Quantity_i     = int(i['Quantity'])
                     s=Store_detail.objects.get(id=Store_i)
                     p=Product_detail.objects.get(id=Product_i)      

                     Order_data = Order_detail(User=User_det,Store=s,Product=p,Quantity=Quantity_i,Ordered_at=x)
                     Order_data.save()
                mes = {
                      'message': 'Order Placed Successfully!'
                         }
                return JsonResponse(mes,status=200,safe=False)      

           else:
                   mes = { 
                        'message' :'No User Found!'
                    }
                   return JsonResponse(mes,status=403,safe=False)



def User_Order_History(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d       = data['Token']
        Key_d         = data['Key']
        if (Key_d == 69):

             if (User_Security.objects.filter(Token = Token_d).exists()):

                 User_s       =User_Security.objects.filter(Token = Token_d)[0]
                 Email_d      = User_s.Email
                 User_list    = User_detail.objects.filter(Email = Email_d)[0]

                 if(Order_detail.objects.filter(User = User_list).exists()):

                     Order_d       =Order_detail.objects.filter(User=User_list)
                     Order_de      =Order_detail.objects.filter(User=User_list)[0]
                     Order_stat    = Order_de.Order_Status
                     Ordered       = Order_de.Ordered_at
                     Order_det     = list(Order_d.values('Store','Product','Quantity','Order_Status','Ordered_at'))
                     data = []
                     for order in Order_det:
                       s = Store_detail.objects.get(id=order["Store"])
                       p = Product_detail.objects.get(id=order["Product"])
                       data.append({"Store_name": s.Store_Name, "Product_name": p.Product_Name,"Product_price":p.Product_Price, "quantity": order["Quantity"], "Geo_loc":s.Geo_Location,"Orderstat":Order_stat,"Orderedat":Ordered})
                     mes = { 
                        'message' :'Your Order History!',
                        'Order_data':data
                         }
                     return JsonResponse(mes,status=200,safe=False)
               
                 else:
                   mes = { 
                        'message' :'No Order Yet!'
                    }
                   return JsonResponse(mes,status=200,safe=False)


def Order_Status_display(request):
    if request.method == 'POST':      
        data = json.loads(request.body)
        Key_d         = data['Key']
        Token_d       = data['Token']
        if (Key_d == 69):

            if (Store_Security.objects.filter(Token = Token_d).exists()):

               Store_s       =Store_Security.objects.filter(Token = Token_d)[0]
               Email_d       = Store_s.Email 
               Store_list    = Store_detail.objects.filter(Email = Email_d)[0]
               

               if(Order_detail.objects.filter(Store = Store_list).exists()):
                   Order_d       =Order_detail.objects.filter(Order_Status="Pending",Store=Store_list)
                   Order_det     = list(Order_d.values('id','User','Product','Quantity','Order_Status','Ordered_at'))
                   data = []
                   for order in Order_det:
                       u = User_detail.objects.get(id=order["User"])
                       p = Product_detail.objects.get(id=order["Product"])
                       data.append({"User_name": u.Name, "Product_name": p.Product_Name,"Product_price":p.Product_Price, "quantity": order["Quantity"], "Geo_loc":u.Geo_Location, "Order_id":order["id"],"Orderstat":"Order_Status","Orderedat":"Ordered_at"})


                   mes = { 
                        'message' :'You have some pending order!',
                        'Order_data':data
                         }
                   return JsonResponse(mes,status=200,safe=False)
               
               else:
                   mes = { 
                        'message' :'No Pending Order!'
                    }
                   return JsonResponse(mes,status=200,safe=False)


def Order_Status_disp(request):
    if request.method == 'POST':      
        data = json.loads(request.body)
        Key_d         = data['Key']
        Token_d       = data['Token']
        if (Key_d == 69):

            if (Store_Security.objects.filter(Token = Token_d).exists()):

               Store_s       =Store_Security.objects.filter(Token = Token_d)[0]
               Email_d       = Store_s.Email 
               Store_list    = Store_detail.objects.filter(Email = Email_d)[0]
               

               if(Order_detail.objects.filter(Store = Store_list).exists()):
                   Order_d       =Order_detail.objects.filter(Order_Status="Delivered",Store=Store_list)
                   Order_det     = list(Order_d.values('id','User','Product','Quantity','Order_Status','Ordered_at'))
                   data = []
                   for order in Order_det:
                       u = User_detail.objects.get(id=order["User"])
                       p = Product_detail.objects.get(id=order["Product"])
                       data.append({"User_name": u.Name, "Product_name": p.Product_Name,"Product_price":p.Product_Price, "quantity": order["Quantity"], "Geo_loc":u.Geo_Location, "Order_id":order["id"],"Orderstat":"Order_Status","Orderedat":"Ordered_at"})


                   mes = { 
                        'message' :'Delivered Order!',
                        'Order_data':data
                         }
                   return JsonResponse(mes,status=200,safe=False)
               
               else:
                   mes = { 
                        'message' :'No Order Delivered!'
                    }
                   return JsonResponse(mes,status=200,safe=False)

def Order_Status_upd(request):
                      
    if request.method == 'POST':
        data = json.loads(request.body)
        Order         = data['Order_id']
        Key_d         = data['Key']
        Token_d       = data['Token']
        if (Key_d == 69):

            if (Store_Security.objects.filter(Token = Token_d).exists()):

               Store_s       =Store_Security.objects.filter(Token = Token_d)[0]
               Email_d       = Store_s.Email 
               Store_list    = Store_detail.objects.filter(Email = Email_d)[0]

               if(Order_detail.objects.filter(Store = Store_list).exists()):

                     if(Order_detail.objects.filter(id = Order).exists()):
                        
                        obj = Order_detail(id=Order,Order_Status="Delivered")
                        obj.save(update_fields=['Order_Status'])
                        mes = { 
                        'message' :'Order Status Updated Successfully!',
                         }
                        return JsonResponse(mes,status=200,safe=False) 
                     else:
                         mes = { 
                              'message' :'Error!'
                          }
                         return JsonResponse(mes,status=200,safe=False)   
             

         

def Product_delete(request):
    
    if request.method == "POST":
        data = json.loads(request.body)
        Product = data['Product_id']
        Key_d         = data['Key']
        Token_d       = data['Token']
        if (Key_d == 69):

           if (Store_Security.objects.filter(Token = Token_d).exists()):
                
            Store_s       =Store_Security.objects.filter(Token = Token_d)[0]
            Email_d       = Store_s.Email 
            Store_list    = Store_detail.objects.filter(Email = Email_d)[0]

            if(Product_detail.objects.filter(Store = Store_list).exists()):
                if(Product_detail.objects.filter(id = Product).exists()):  
                   obj = get_object_or_404(Product_detail, id=Product)
                   obj.delete()                   
                   mes = { 
                   'message' :'Product Deleted Successfully!',
                    }
                   return JsonResponse(mes,status=200,safe=False)
