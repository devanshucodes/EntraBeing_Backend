from django.urls import path
from Inno_Extrabeing.views import User_registration_view,User_login_view,Store_registration_view,Store_login_view,Product_registration_view,User_dash,Product_dash,Store_dash,Cart_View,User_Logout,Store_Logout,Order_Status_display,Order_View,User_Order_History,Order_Status_disp,Order_Status_upd,Product_delete


app_name = 'Inno_Extrabeing'
urlpatterns = [
 	 path('User/registration', User_registration_view, name="User_register"),
    path('User/login', User_login_view, name="User_login"),
    path('Store/registration', Store_registration_view, name="Store_register"),
    path('Store/login', Store_login_view, name="Store_login"),
    path('Product/registration', Product_registration_view, name="Product_register"),
    path('User/home', User_dash, name="User_dashb"),
    path('Store/Product', Product_dash, name="Product_dashb"),
    path('Store/home', Store_dash, name="Store_dashb"),
    path('User/cart', Cart_View, name="Cart_Viewb"),
    path('User/logout', User_Logout, name="User_Logoutb"),
    path('Store/logout', Store_Logout, name="Store_Logoutb"),
    path('Store/Order/Status', Order_Status_display, name="Order_Status_displayb"),
    path('Store/Order', Order_View, name="Order_Viewb"),
    path('User/Order/History', User_Order_History, name="User_Order_Historyb"),
    path('Store/Order/History', Order_Status_disp, name="Order_Status_dispb"),
    path('Store/Order/Status/upd', Order_Status_upd, name="Order_Status_updb"),
    path('Product/delete', Product_delete, name="Product_deleteb"),

   ]