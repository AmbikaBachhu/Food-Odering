from django.urls import path
from Admins import views

urlpatterns = [
    path('',views.all,name="all"),
    path('place/',views.place,name="place"),
    path('save_place/',views.saveplace,name="save_place"),
    path('view_place/',views.viewplace,name="view_place"),
    path('update_places/', views.updateplace, name="update_places"),
    path('save_update/', views.saveupdate, name="save_update"),
    path('delete_places/',views.deleteplace,name="delete_places"),
    path('cat/', views.cat, name="cat"),
    path('save_category/',views.savecategory,name="save_category"),
    path('view_category/',views.viewcategory,name="view_category"),
    path('update_category/', views.updatecategory, name="update_category"),
    path('save_updatecategory/', views.saveupcat, name="save_updatecat"),
    path('delete_category/',views.deletecategory,name="delete_category"),
    path('food_type/', views.food_type, name="food_type"),
    path('save_foodtype/', views.save_foodtype, name="save_foodtype"),
    path('view_foodtype/', views.view_foodtype, name="view_foodtype"),
    path('update_foodtype/', views.updatefood_type, name="update_foodtype"),
    path('save_updatefoodtype/', views.saveupftype, name="save_updatefoodtype"),
    path('delete_foodtype/',views.deletefood_type,name="delete_foodtype"),

]