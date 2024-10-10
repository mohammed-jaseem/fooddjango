from django.urls import path
from manager import views

app_name = "manager"


urlpatterns = [
    path('',views.index, name='index'),
    path('foodcategories',views.foodcategories, name='foodcategories'),
    path('foodcategories_add',views.foodcategories_add, name='foodcategories_add'),
    # path('edit_foodcategories',views.edit_foodcategories, name='edit_foodcategories'),
    path('delete_foodcategories/<int:id>/',views.delete_foodcategories, name='delete_foodcategories'),
    path('offers',views.offers, name='offers'),
    path('offers_add',views.offers_add, name='offers_add'),
    # path('edit_offer',views.edit_offer, name='edit_offer'),
    path('delete-offers',views.delete_offers, name='delete_offers'),
    path('foods',views.foods, name='foods'),
    path('foods_add',views.foods_add, name='foods_add'),
    # path('edit_foods',views.edit_foods, name='edit_foods'),
    path('delete_foods',views.delete_foods, name='delete_foods'),
    # path('orders',views.orders, name='orders')
    path('restaurants',views.restaurants, name='restaurants'),
    path('restaurants_add',views.restaurants_add, name='restaurants_add'),
    path('edit_restaurants',views.edit_restaurants, name='edit_restaurants'),
    path('delete_restaurants/<int:id>/',views.delete_restaurants, name='delete_restaurants'),
    path('slideries',views.slideries, name='slideries'),
    path('slideries_add',views.slideries_add, name='slideries_add'),
    path('edit_slideries/<int:id>/',views.edit_slideries, name='edit_slideries'),
    path('delete_slideries/<int:id>/',views.delete_slideries, name='delete_slideries'),
    path('restaurant_categories',views.restaurant_categories, name='restaurant_categories'),
    path('add_restaurant_categories',views.add_restaurant_categories, name='add_restaurant_categories'),
    path('edit_restaurant_categories/<int:id>/',views.edit_restaurant_categories, name='edit_restaurant_categories'),
    path('delete_restaurant_categories/<int:id>/',views.delete_restaurant_categories, name='delete_restaurant_categories'),
    path('users',views.users, name='users'),
    path('delete_users/<int:id>/',views.delete_users, name='delete_users'),
    path('edit_users/<int:id>/',views.edit_users, name='edit_users'),
    path('orders',views.orders, name='orders'),
    path('orders_add',views.orders_add, name='orders_add'),
    path('edit_orders/<int:id>/',views.edit_orders, name='edit_orders'),
    path('delete_orders/<int:id>/',views.delete_orders, name='delete_orders'),

]
    
   