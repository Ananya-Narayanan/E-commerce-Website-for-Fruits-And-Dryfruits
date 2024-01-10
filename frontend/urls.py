from django.urls import path
from frontend import views
urlpatterns=[
    path('homepg/',views.homepg,name="homepg"),
    path('propg/',views.propg,name="propg"),
    path('singlepro/<int:proid>/',views.singlepro,name="singlepro"),
    path('profilter/<cat_name>/',views.profilter,name="profilter"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('services/',views.services,name="services"),
    path('savedata/',views.savedata,name="savedata"),
    path('register/',views.register,name="register"),
    path('saveregister/',views.saveregister,name="saveregister"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('logout/',views.logout,name="logout"),
    path('cart/',views.cart,name="cart"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('delete_cart/<int:dataid>/',views.delete_cart,name="delete_cart"),
    path('checkout/', views.checkout, name="checkout"),


]