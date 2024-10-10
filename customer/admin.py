from django.contrib import admin

from customer.models import Customer,Cart,CartBill,Offer,Address,Order,OrderItem

admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartBill)
admin.site.register(Offer)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)






