from django.shortcuts import render, reverse
from restaurant.models import *
from customer.models import *
from django.http import HttpResponseRedirect
from manager.forms import *
from main.functions import generate_form_errors



def index(request):
    
    return render(request,'manager/index.html')

def restaurant_categories(request):
    instances = RestaurantCategory.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/restaurant_categories.html', context=context)

def delete_restaurant_categories(request,id):
    instance = RestaurantCategory.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:restaurant_categories'))

def add_restaurant_categories(request,):
    if request.method == 'POST':   
        form = RestaurantCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:restaurant_categories'))
            
        else:
            message = generate_form_errors(form)
            form = RestaurantCategoryForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/add_restaurant_categories.html', context=context)



    else:
        form = RestaurantCategoryForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/add_restaurant_categories.html', context=context)

def edit_restaurant_categories(request, id):
    instance = RestaurantCategory.objects.get(id=id)
    if request.method == 'POST':   
        form = RestaurantCategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:restaurant_categories'))
            
        else:
            message = generate_form_errors(form)
            form = RestaurantCategoryForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/add_restaurant_categories.html', context=context)



    else:
        form = RestaurantCategoryForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/add_restaurant_categories.html', context=context)

def restaurants(request):
    instances = Restaurant.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/restaurants.html', context=context)

def delete_restaurants(request,id):
    instance = Restaurant.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:restaurants'))

def restaurants_add(request,):
    if request.method == 'POST':   
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:restaurants'))
            
        else:
            message = generate_form_errors(form)
            form = RestaurantForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/restaurants_add.html', context=context)



    else:
        form = RestaurantForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/restaurants_add.html', context=context)

def edit_restaurants(request, id):
    instance = Restaurant.objects.get(id=id)
    if request.method == 'POST':   
        form = RestaurantForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:restaurants'))
            
        else:
            message = generate_form_errors(form)
            form = RestaurantForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/restaurants_add.html', context=context)

def restaurants(request):
    instances = Restaurant.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/restaurants_add.html', context=context)

def slideries(request):
    instances = Slider.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/slideries.html', context=context)

def delete_slideries(request,id):
    instance = Slider.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:slideries'))

def slideries_add(request,):
    if request.method == 'POST':   
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:slideries'))
            
        else:
            message = generate_form_errors(form)
            form = SliderForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/slideries_add.html', context=context)



    else:
        form = SliderForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/slideries_add.html', context=context)

def edit_slideries(request, id):
    instance = Slider.objects.get(id=id)
    if request.method == 'POST':   
        form = SliderForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:slideries'))
            
        else:
            message = generate_form_errors(form)
            form = SliderForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/slideries_add.html', context=context)



    else:
        form = SliderForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/slideries_add.html', context=context)





def foodcategories(request):
    instances = FoodCategory.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/foodcategories.html', context=context)

def delete_foodcategories(request,id):
    instance = FoodCategory.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:foodcategories'))

def foodcategories_add(request,):
    if request.method == 'POST':   
        form = FoodCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:foodcategories'))
            
        else:
            message = generate_form_errors(form)
            form = FoodCategoryForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/foodcategories_add.html', context=context)



    else:
        form = FoodCategoryForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/foodcategories_add.html', context=context)





def foods(request):
    instances = Food.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/foods.html', context=context)

def delete_foods(request,id):
    instance = Food.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:foods'))

def foods_add(request,):
    if request.method == 'POST':   
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:foods'))
            
        else:
            message = generate_form_errors(form)
            form = FoodForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/foods_add.html', context=context)



    else:
        form = FoodForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/foods_add.html', context=context)



def users(request):
    instances = User.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/users.html', context=context)

def delete_users(request,id):
    instance = User.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:users'))

def edit_users(request, id):
    instance = User.objects.get(id=id)
    if request.method == 'POST':   
        form = UserForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:users'))
            
        else:
            message = generate_form_errors(form)
            form = UserForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/users_add.html', context=context)



    else:
        form = UserForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/users_add.html', context=context)



def offers(request):
    instances = Offer.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/offers.html', context=context)

def delete_offers(request,id):
    instance = Offer.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:offers'))

def offers_add(request,):
    if request.method == 'POST':   
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:offers'))
            
        else:
            message = generate_form_errors(form)
            form = OfferForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/offers_add.html', context=context)



    else:
        form = OfferForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/offers_add.html', context=context)



def orders(request):
    instances = Order.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/orders.html', context=context)

def delete_orders(request,id):
    instance = Order.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:orders'))

def orders_add(request,):
    if request.method == 'POST':   
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:orders'))
            
        else:
            message = generate_form_errors(form)
            form = OrderForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/orders_add.html', context=context)



    else:
        form = OrderForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/orders_add.html', context=context)

def edit_orders(request, id):
    instance = Order.objects.get(id=id)
    if request.method == 'POST':   
        form = OrderForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:orders'))
            
        else:
            message = generate_form_errors(form)
            form = OrderForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/orders_add.html', context=context)



    else:
        form = OrderForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/orders_add.html', context=context)

    


