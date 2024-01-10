from django.urls import path
from foodapp import views

urlpatterns=[
    path('foodpg/',views.foodpg,name="foodpg"),
    path('foodcat/',views.foodcat,name="foodcat"),
    path('savecat/',views.savecat,name="savecat"),
    path('discat/',views.discat,name="discat"),
    path('editcat/<int:dataid>/',views.editcat,name="editcat"),
    path('updatecat/<int:dataid>/',views.updatecat,name="updatecat"),
    path('deletecat/<int:dataid>/',views.deletecat,name="deletecat"),
    path('fooditem/',views.fooditem,name="fooditem"),
    path('saveitem/',views.saveitem,name="saveitem"),
    path('disitem/',views.disitem,name="disitem"),
    path('edititem/<int:dataid>/',views.edititem,name="edititem"),
    path('updateitem/<int:dataid>/',views.updateitem,name="updateitem"),
    path('deleteitem/<int:dataid>/', views.deleteitem, name="deleteitem"),
    path('adm/',views.adm,name="adm"),
    path('adminlog/',views.adminlog,name="adminlog"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('viewcontact/',views.viewcontact,name="viewcontact"),
    path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact"),
    path('dis_iitem/',views.dis_iitem,name="dis_iitem"),



]
