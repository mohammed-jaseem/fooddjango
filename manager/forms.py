from django import forms
from restaurant.models import *
from users.models import User
from customer.models import *




class RestaurantCategoryForm(forms.ModelForm):
    class Meta:
        model = RestaurantCategory
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'category title'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
        
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['title', 'restaurant_category', 'image', 'short_discription', 'rating', 'timer']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Restaurant title'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'restaurant_category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'restaurant_category'}),
            'short_discription': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'short_discription'}),  
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating'}),
            'timer': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Time in minutes'}),
        }

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['image', 'restaurant']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'restaurant': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ['name', 'restaurant']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'restaurant': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price', 'is_veg', 'image', 'restaurant', 'foodcategory']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'is_veg': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'restaurant': forms.Select(attrs={'class': 'form-control'}),
            'foodcategory': forms.Select(attrs={'class': 'form-control'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'is_customer', 'is_store', 'is_agent', 'is_manager']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'is_customer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_store': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_agent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_manager': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['code', 'discount', 'short_description', 'is_percentage']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Offer Code'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Discount Amount'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short Description'}),
            'is_percentage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer',
            'address',
            'order_id',
            'item_totel',
            'offer_amount',
            'totel_amount',
            'delivery',
        ]
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Select(attrs={'class': 'form-control'}),
            'order_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Order ID'}),
            'item_totel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Item Total'}),
            'offer_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Offer Amount'}),
            'totel_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Amount'}),
            'delivery': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Delivery Charge'}),
        }