from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CartItem, Customer, Product, Contact, Order

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def menu(request):
    return render(request, 'shop/main.html')

def shop(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/e_commerce.html', context=context)

def product(request, slug=None):
    if slug is not None:
        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            messages.add_message(request, "Product Doesn't exist")
            return redirect('/shop')
        context = {
            'product': product
        }
        return render(request, 'shop/product.html', context=context)
    return redirect('/shop')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, 'Wrong username or password')
            return redirect('/login')
        login(request, user)
        if 'next' in request.POST:
            return redirect(request.POST['next'])
        return redirect('/shop')
    next_url = '/shop/'
    if 'next' in request.GET:
        next_url = request.GET['next']
    return render(request, 'shop/login.html', {'next_url':next_url})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully")
    return redirect('/menu')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpass']
        phone = request.POST['phone']
        address = request.POST['address']
        if password!=confirm_password:
            messages.warning(request, 'Password didn\'t match! Retry')
            return redirect('/signup')
        try:
            check = User.objects.get(username=username)
            messages.warning(request, 'Username already exists, try using another one')
            return redirect('/signup')
        except:
            pass
        try:
            check = User.objects.get(email=email)
            messages.warning(request, 'Email already exists, try using another one')
            return redirect('/signup')
        except:
            pass
        try:
            check = Customer.objects.get(phone=phone)
            messages.warning(request, 'Phone number already exists, try using another one')
            return redirect('/signup')
        except:
            pass
        user = User.objects.create(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
        user.save()
        customer = Customer(user=user, phone=phone, address=address)
        customer.save()
        login(user)
        return redirect('/shop')
    return render(request, 'shop/signup.html')

def events(request):
    return render(request, 'shop/events.html')

@login_required(login_url='/login')
def cart(request):
    if request.method=='POST':
        id = request.POST['id']
        try:
            product = Product.objects.get(id=id)
            customer = Customer.objects.get(user=request.user)
        except:
            return redirect('/shop')
        cart_item = CartItem(product=product, customer=customer, quantity=1, price=product.price)
        cart_item.save()
        return redirect('/cart')
    customer = Customer.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(customer=customer)
    count = len(cart_items)
    amount = 0.0
    shipping_charges = 50.0
    for item in cart_items:
        amount += item.quantity * item.product.price
    context = {
        'items': cart_items,
        'count': count,
        'amount': amount,
        'shipping': shipping_charges
    }
    return render(request, 'shop/cart.html', context=context)

@login_required(login_url='/login')
def removeCartItem(request):
    if request.method=="POST":
        id = request.POST['id']
        try:
            item = CartItem.objects.get(id=id)
        except:
            return redirect('/cart')
        item.delete()
    return redirect('/cart')

@login_required(login_url="/login")
def order(request):
    return render(request, 'shop/order_sum.html')

def about(request):
    return render(request, 'shop/about_us.html')

def support(request):
    return render(request, 'shop/support.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['message']
        entry = Contact(name=name, email=email, query=query)
        entry.save()
        messages.success(request, "Thankyou for contacting us.")
        return redirect('/menu')
    return render(request, 'shop/contact_us.html')

def checkout(request):
    customer = Customer.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(customer=customer)
    if request.method=='POST':
        for item in cart_items:
            order = Order(customer=customer, product=item.product, quantity=item.quantity, price=item.price, status='placed')
            order.save()
            item.delete()
        messages.success(request, 'Order placed successfully')
        return redirect('/menu')
    count = len(cart_items)
    amount = 0.0
    shipping_charges = 50.0
    for item in cart_items:
        amount += item.quantity * item.product.price
    if count>0:
        amount += shipping_charges
    context = {
        'items': cart_items,
        'count': count,
        'amount': amount,
        'customer': customer
    }
    return render(request, 'shop/checkout.html', context=context)

