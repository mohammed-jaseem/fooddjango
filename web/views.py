from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required

from users.models import User
from customer.models import *
from restaurant.models import Slider, RestaurantCategory,Restaurant,Food,FoodCategory
from django.db.models import Sum

@login_required(login_url='/login')
def index(request):
    slideries = Slider.objects.all()
    restaurant_categories = RestaurantCategory.objects.all()
    restaurants = Restaurant.objects.all()
  
    context = {
        "slideries": slideries,
        "restaurant_categories":restaurant_categories,
        "restaurants":restaurants,
    }
    return render(request, 'web/index.html', context=context)

@login_required(login_url='/login')
def singlerest(request,id):
    user = request.user
    customer = Customer.objects.get(user=user)
    restaurant = Restaurant.objects.get(id=id)
    foods = Food.objects.filter(restaurant=restaurant)
    foodcategory = FoodCategory.objects.filter(restaurant=restaurant) 
    carts = Cart.objects.filter(restaurant=restaurant,customer=customer)

    cart_quantities = {cart.product: cart.quantity for cart in carts}
    prod_with_qty =[(food, cart_quantities.get(food, 0)) for food in foods]

    context = {
        "restaurant":restaurant,
        "foods":foods,
        "foodcategory":foodcategory,
        "prod_with_qty":prod_with_qty,

    }
    return render(request, 'web/singlerest.html', context=context)

def cart(request):
    customer = Customer.objects.get(user=request.user)
    cart_items = Cart.objects.filter(customer=customer)
    if Cart.objects.filter(customer=customer).exists():
        restaurant = cart_items.first().restaurant
        cart_amount = cart_items.aggregate(Sum('price'))['price__sum']
    else:
        restaurant = None
        cart_amount = 0
    delivery = 50
    discount = 0



    if CartBill.objects.filter(customer=customer).exists():
        cartbill = CartBill.objects.get(customer=customer)
        cartbill.item_totel=cart_amount
        cartbill.totel_amount=cart_amount + delivery - float(cartbill.offer_amount)
        cartbill.save()
    
    else:
        cartbill = CartBill.objects.create(
            customer=customer,
            item_totel=cart_amount,
            delivery=delivery,
            totel_amount=cart_amount + delivery,
            offer_amount=0,
        )

    if request.method == 'POST':
        code = request.POST.get('code')
        offer = Offer.objects.get(code=code)
        if offer.is_percentage:
            discount = (offer.discount / 100) * cart_amount
            discount = round(discount)
            cartbill.offer_amount = discount
            cartbill.totel_amount=cart_amount + delivery - float(discount)
            cartbill.save()
        else:
            discount = offer.discount
            cartbill.offer_amount = discount
            cartbill.totel_amount=cart_amount + delivery - float(discount)
            cartbill.save()


    address = cartbill.address

    context = {
       "customer":customer,
       "cart_items":cart_items,
       "restaurant":restaurant,
       "cart_amount":cart_amount,
       "cartbill":cartbill,
       "discount":discount,
       "address": address,
    }


    return render(request, 'web/cart.html', context=context)

@login_required(login_url='/login')
def add_address(request):
    user = request.user
    customer = Customer.objects.get(user=user)

    if request.method == 'POST':
        address = request.POST.get('address')
        appartment = request.POST.get('appartment')
        landmark = request.POST.get('landmark')
        address_type = request.POST.get('address_type')

        address = Address.objects.create(
            customer=customer,
            address=address,
            appartment=appartment,
            landmark=landmark,
            address_type=address_type,
        )
        address.save()
        return HttpResponseRedirect(reverse('web:address'))
    else:    
        return render(request, 'web/add-address.html',)
    
@login_required(login_url='/login')
def address(request):
    customer = Customer.objects.get(user=request.user)
    current_address = Address.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'current_address': current_address,
    }

    return render(request, 'web/address.html', context=context)

@login_required(login_url='/login')
def address_delete(request, id):
    address = Address.objects.get(id=id)
    address.delete()
    
    return HttpResponseRedirect(reverse('web:address'))

@login_required(login_url='/login/')
def address_edit(request,id):            
    user =request.user
    customer = Customer.objects.get(user=user)
    address = Address.objects.get(id=id, customer=customer)

    if request.method == 'POST':
        address = request.POST.get('address')
        appartment = request.POST.get('appartment')
        landmark = request.POST.get('landmark')
        address_type = request.POST.get('address_type')
        
        address = Address.objects.create(
            customer=customer,
            address=address,
            appartment=appartment,
            landmark=landmark,
            address_type=address_type,
        )
        address.save()
        return HttpResponseRedirect(reverse('web:address'))
    
    else:
        return render(request, 'web/add-address.html', {'address': address, 'is_edit': True})
    

@login_required(login_url='/login/')
def address_select(request,id):   
    user = request.user
    customer = Customer.objects.get(user=user)
    address = Address.objects.get(id=id)
    cartbill = CartBill.objects.get(customer=customer)
    cartbill.address=address
    cartbill.save()

    return HttpResponseRedirect (reverse('web:cart'))

def offer(request):

    return render(request, 'web/offer.html',)


@login_required(login_url='/login/')
def restaurants(request,id):
    restaurant_categories = RestaurantCategory.objects.all()
    category = RestaurantCategory.objects.get(id=id)
    restaurant = Restaurant.objects.filter(restaurant_category=category)
    
    context = {
        "restaurant_categories": restaurant_categories,
        "restaurant": restaurant,
        "category" : category,
        
        
    }
    return render(request, 'web/restaurants.html', context=context)


@login_required(login_url='/login')
def add_cart(request, id):
    customer = Customer.objects.get(user=request.user)
    product = Food.objects.get(id=id)
    cart= Cart.objects.create(
        product=product, 
        customer=customer,
        quantity=1,
        price=product.price,
        restaurant=product.restaurant,        
    )
    cart.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login')
def plus_cart(request, id):
    customer = Customer.objects.get(user=request.user)  
    product = Food.objects.get(id=id)
    cart = Cart.objects.get(product=product, customer=customer)
    cart.quantity += 1
    cart.price += product.price
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login')
def minus_cart(request, id):
    customer = Customer.objects.get(user=request.user)
    product = Food.objects.get(id=id)
    cart = Cart.objects.get(product=product, customer=customer)
    cart.quantity -= 1
    cart.price -= product.price
    if cart.quantity == 0:
        cart.delete()
    else:
        cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 

        user = authenticate(request, email=email, password=password,) 

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            context = {
                'error':True,
                'message':'Invalid email or password'
            }
            return render(request, 'web/login.html', context=context)
    else:
        return render(request, 'web/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            email=email,
            password=password,
            is_customer=True
        )
        user.save()
        customer = Customer.objects.create(
            user=user
        )
        customer.save()
        return HttpResponseRedirect(reverse('web:login'))
    else:
        return render(request, 'web/register.html')
    
def logout(request):
    user = request.user
    auth_logout(request)

    return HttpResponseRedirect(reverse('web:login'))

@login_required(login_url='/login')
def checkout(request):
    user = request.user
    customer = Customer.objects.get(user=user)

    try:
        cartbill = CartBill.objects.get(customer=customer)
    except CartBill.DoesNotExist:
        cartbill = None

    context = {
        'item_totel': cartbill.item_totel if cartbill else 0, 
        'offer_amount': cartbill.offer_amount if cartbill else 0,
        'delivery': cartbill.delivery if cartbill else 0,
        'totel_amount': cartbill.totel_amount if cartbill else 0,
    }


    return render(request, 'web/checkout.html',context=context)


@login_required(login_url='/login/')
def create_order(request): 
    user = request.user
    customer = Customer.objects.get(user=user)
    cart_items = Cart.objects.filter(customer=customer) 
    cartbill = CartBill.objects.get(customer=customer)
    
    order = Order.objects.create(
        customer=customer,
        delivery = cartbill.delivery,
        item_totel = cartbill.item_totel,
        offer_amount = cartbill.offer_amount,
        address = cartbill.address,
        totel_amount = cartbill.totel_amount,
    )
    
    order.save()
    
    
    for cart in cart_items:
        order_item = OrderItem.objects.create(
        customer=customer,
        order=order,
        restaurant=cart.restaurant,
        quantity=cart.quantity,
        price=cart.price,
        product=cart.product
        )       
    
        order_item.save()
        cart.delete()

    previous_order = Order.objects.all().order_by('-id').first()
    
    
    if previous_order is not None:
        last_id = previous_order.id
        order_id = f'ORD{last_id + 1:03d}'
    else:
        order_id = "ORD001"

    order.order_id = order_id
    order.save()
        
        
    return HttpResponseRedirect (reverse('web:order'))


@login_required(login_url='/login/')
def single_order(request,id):
    user = request.user
    customer = Customer.objects.get(user=user)
    order = Order.objects.get(id=id) 
    
    
    context = {
        'order': order, 
        'customer': customer, 
        }
    return render(request, 'web/single_order.html', context=context) 
    

@login_required(login_url='/login/')
def order(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    orders = Order.objects.filter(customer=customer).prefetch_related('order_item')   
    
    
    context = {
        'orders': orders,  
        }
    return render(request, 'web/order.html', context=context) 
def account(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    order = Order.objects.filter(customer=customer).prefetch_related('order_item')[:3]
    
    
    context = {
        'order': order,  
        }
    return render(request, 'web/account.html', context=context)

