from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/",views.logout, name="logout"),
    path("singlerest/<int:id>/",views.singlerest, name="singlerest"),
    path("cart/",views.cart, name="cart"),
    path("add-address/",views.add_address, name="add-address"),
    path("add_cart/<int:id>/",views.add_cart, name="add_cart"),
    path("plus_cart/<int:id>/",views.plus_cart, name="plus_cart"),
    path("minus_cart/<int:id>/",views.minus_cart, name="minus_cart"),
    path("address/",views.address, name="address"),
    path("offer/",views.offer, name="offer"),
    path('restaurants/<int:id>/', views.restaurants, name='restaurants'),
    path("address/delete/<int:id>/",views.address_delete, name="address_delete"),
    path("address/edit/<int:id>/",views.address_edit, name="address_edit"),
    path("address_select/<int:id>/",views.address_select, name="address_select"),
    path("checkout/",views.checkout, name="checkout"),
    path("create_order/",views.create_order, name="create_order"),
    path("order/",views.order, name="order"),
    path("account/",views.account, name="account"),
    path("single_order/<int:id>/",views.single_order, name="single_order"),

]