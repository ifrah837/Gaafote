from django.shortcuts import render
from.models import Product,Cart,CartItem,Category
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Product, Cart, CartItem,Category 
def Mobile_view(request): 
    category= get_object_or_404(Category , name='Apple Phones') 
    products=Product.objects.filter(category=category) 
    return render(request,'Mobile.html',{'category':Category,'products':products}) 

def product_list(request): 
    categories = Category.objects.all() 
    
    products = Product.objects.all() 
    return render(request, 'index.html', {'products': products, 'categories': categories}) 

# function kani waxa uu ino ogalanaya in aynu cartiga wax ku ridano 
def add_to_cart(request, product_id): 
    product = get_object_or_404(Product, id=product_id) 
     
    # Get the cart or create one if it doesn't exist 
    cart, created = Cart.objects.get_or_create(user=request.user) 
     
    # Check if the product is already in the cart 
    cart_item, created = CartItem.objects.get_or_create(cart=cart, 
product=product) 
     
    if not created: 
        # If the item already exists, just increase the quantity 
        cart_item.quantity += 1 
        cart_item.save() 
     
    return redirect('view_cart') 
 
# View Cart 
def view_cart(request): 
    cart = Cart.objects.get(user=request.user) 
    cart_items = cart.cartitem_set.all() 
    total = cart.total 
 
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': 
total})
 
 
 