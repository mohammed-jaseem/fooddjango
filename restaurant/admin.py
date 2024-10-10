from django.contrib import admin
from restaurant.models import RestaurantCategory, Restaurant, Slider, Food, FoodCategory


admin.site.register(RestaurantCategory)
admin.site.register(Restaurant)
admin.site.register(Slider)
admin.site.register(Food)
admin.site.register(FoodCategory)