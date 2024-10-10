from django.db import models

    
class RestaurantCategory(models.Model):
    image = models.ImageField(upload_to="restaurant_category")
    title = models.CharField(max_length=225)

    class Meta:
        db_table = "restaurant_Restaurant_Category"
        verbose_name = "Restaurant_Category"
        verbose_name_plural = "Restaurant_Categories"
        ordering = ["-id"]

    def __str__(self):
        return self.title
    
class Restaurant(models.Model):
    image = models.ImageField(upload_to="Restaurant")
    title = models.CharField(max_length=225)
    short_discription = models.CharField(max_length=225)
    rating = models.FloatField()
    timer = models.IntegerField()
    restaurant_category = models.ForeignKey(RestaurantCategory, on_delete=models.CASCADE)
    

    class Meta:
        db_table = "restaurant_restaurant"
        verbose_name = "restaurant"
        verbose_name_plural = "restaurants"
        ordering = ["-id"]

    def __str__(self):
        return self.title


class Slider(models.Model):
    image = models.ImageField(upload_to="Restaurant_Category")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = "restaurant_slider"
        verbose_name = "slider"
        verbose_name_plural = "slideries"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)

class FoodCategory(models.Model):   
    name = models.CharField(max_length=225)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


    class Meta:
        db_table = "foodcategory"
        verbose_name = "foodcategory"
        verbose_name_plural = "foodcategories"
        ordering = ["-id"]

    def __str__(self):
        return self.name

class Food(models.Model):
    image = models.ImageField(upload_to="Food")
    name = models.CharField(max_length=225)
    price = models.FloatField()
    is_veg = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    foodcategory = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)


    class Meta:
        db_table = "food"
        verbose_name = "food"
        verbose_name_plural = "foods"
        ordering = ["-id"]

    def __str__(self):
        return self.name
