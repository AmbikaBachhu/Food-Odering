from django.urls import path,re_path
from foodapp import views
from django.views.generic import ListView
from foodapp.models import Place
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ListView.as_view(model=Place,
                                   template_name='food/place.html'),name="home"),
    re_path(r'^place/(?P<place_id>\d+)/$', views.choose_restaurant, name='restaurant'),
    re_path(r'^place/(?P<place_id>\d+)/rest/(?P<rest_id>\d+)/$', views.choose_food, name='food'),
    re_path(r'^place/(?P<place_id>\d+)/$', views.rest_price, name='rest_price'),
    re_path(r'^place/(?P<place_id>\d+)/$', views.rest_rating, name='rest_rating'),
    path('register/user/', views.customerRegister, name='register'),
    path('register/restaurant/', views.restRegister, name='rregister'),
    path('login/user/', views.customerLogin, name='login'),
    path('login/restaurant/', views.restLogin, name='rlogin'),
    path('profile/user/', views.customerProfile, name='profile'),
    path('profile/restaurant/', views.restaurantProfile, name='rprofile'),
    path('user/create/', views.createCustomer, name='ccreate'),
    path('info/', views.info, name='rcreate'),
    path('info_save/', views.info_save, name='info_save'),
    path('foodie/', views.foodie, name="foodie"),
    path('food_save/', views.food_save, name="food_save"),
    path('update_item/', views.updateitem, name="update_item"),
    path('user/update/<int:id>/', views.updateCustomer, name='cupdate'),
    path('restaurant/update/<int:id>/', views.updateRestaurant, name='rupdate'),
    path('logout/', views.Logout, name='logout'),
    path('update_order/',views.updateorder,name="update_order"),
    path('save_order/', views.saveorder, name="save_order"),
    path('orderplaced/', views.orderplaced,name="orderplaced"),
    path('restaurant/orderlist/', views.orderlist, name='orderlist'),
    path('order_history_user/', views.order_history_user, name='order_history_user'),
    path('order_his/',views.orderhis,name="order_his"),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)