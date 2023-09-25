from django.urls import path
from.views import *
urlpatterns=[
    path('first/',first),
    path('register/',register1),
    path('login/',login_view),
    path('profile/',profile),
    path('edit/<int:id>',editdata),
    path('fileedit/<int:id>',fileedit),
    path('addmoney/<int:id>',addmoney),
    path('success/',success),
    path('widrawmoney/<int:id>',widrawmoney),
    path('widrawdisplay/',widrawdisplay),
    path('checkbalance/<int:id>', checkbalance),
    path('checkbalance1/', checkbalance1),
    path('statement/<int:id>', statement),
    path('depdisplay/', depdisplay),
    path('withdisplay/', withdisplay),
    path('news/', news),
    path('admin/',admin),
    path('newsdisplay/', newsdisplay),
    path('display/', display),
    path('adminnewsdelete/<int:id>', adminnewsdelete),
    path('adminnewsedit/<int:id>', adminnewsedit),
    path('wish/<int:id>',wish),
    path('wishlistview/',wishlistview),
    path('logoutt/',logoutt),
    path('index/',index),
    path('forget/',forgetpassword),
    path('change/<int:id>',change_password)








]