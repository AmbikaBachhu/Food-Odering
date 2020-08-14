import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from foodapp.forms import CustomerSignUpForm, CustomerForm, RestaurantSignUpForm, RestaurantForm, foodForm
from django.contrib.auth.decorators import login_required
from foodapp.utils import cookiecart, cartData
import json
from django.http import JsonResponse
# Create your views here.
from foodapp.models import Place, SubCategory, Food, Food_type, Restaurant, Customer, User, Order, OrderItem, \
    OrderHistory
from django.db.models import Q


# Create your views here.


def choose_restaurant(request, place_id):
    food_list = Food.objects.filter(place_id=place_id)
    rest_list = []
    for f in food_list:
        r = Restaurant.objects.get(id=f.rest_id)
        if r not in rest_list:
            rest_list.append(r)

    context = {
        'place_id': place_id,
        'rest_list': rest_list,

    }
    return render(request, 'food/complete restaurant.html', context)


def rest_price(request, place_id):
    food_list = Food.objects.filter(place_id=place_id)
    rest_list = []
    for f in food_list:
        r = Restaurant.objects.get(id=f.rest_id)
        if r not in rest_list:
            rest_list.append(r)
    rest_prices = rest_list
    rest_prices = sorted(rest_prices, key=lambda ur: (ur.price))
    context = {
        'place_id': place_id,
        'rest_list': rest_list,
        'rest_prices': rest_prices
    }
    return render(request, "food/rest_price.html", context)


def rest_rating(request, place_id):
    food_list = Food.objects.filter(place_id=place_id)
    rest_list = []
    for f in food_list:
        r = Restaurant.objects.get(id=f.rest_id)
        if r not in rest_list:
            rest_list.append(r)
    rest_rate = Restaurant.objects.all()
    rest_rate = sorted(rest_rate, key=lambda ur: (-ur.votes))
    return render(request, "food/rest_rate.html", {"rest_rate": rest_rate})


def choose_food(request, place_id, rest_id):
    food = Food.objects.filter(place_id=place_id, rest_id=rest_id)
    rest = Restaurant.objects.get(id=rest_id)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False, restaurant=rest)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        cookieDate = cookiecart(request)
        cartItems = cookieDate['cartItems']
        order = cookieDate['order']
        items = cookieDate['items']

    context = {
        'rest': rest,
        'food': food,
        'cartitems': cartItems,
        'order': order,
        'items': items,
    }
    return render(request, 'food/foods.html', context)


def updateitem(request):
    data = json.loads(request.body)
    foodId = data['foodId']
    action = data['action']
    print('Action:', action)
    print('FoodId:', foodId)

    customer = request.user.customer
    food = Food.objects.get(id=foodId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, food=food)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


@login_required(login_url='/login/user/')
def updateorder(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    amount = order.get_cart_total
    no = request.GET.get("mn")
    up = Order.objects.filter(id=no)
    context = {
        'cartitems': cartItems,
        'order': order,
        'items': items,
        'up': up,
        'amount': amount
    }
    return render(request, "update_order.html", context)


def saveorder(request):
    no = request.POST.get("id")
    name = request.POST.get("name")
    land = request.POST.get("land")
    amount = request.POST.get("amount")
    Order.objects.filter(id=int(no)).update(door_no=name, landmark=land, total_amount=int(amount), complete=True)
    return redirect('orderplaced')


def orderhis(request):
    user = request.user
    ordered_cust = None
    customers = Customer.objects.all()
    for cust in customers:
        if user.username == cust.user:
            ordered_cust = cust
    if ordered_cust is not None:
        orders1 = OrderItem.objects.filter(user_id__exact=ordered_cust.user_id).order_by('-date_added')
    return render(request, "ordersss.html",{"item":orders1})


def restuarent(request):
    r_object = Restaurant.objects.all()
    query = request.GET.get('q')
    if query:
        r_object = Restaurant.objects.filter(Q(rname__icontains=query)).distinct()
        return render(request, 'restaurant/restaurant.html', {'r_object': r_object})
    return render(request, 'restaurant/restaurant.html', {'r_object': r_object})


# Creating Customer Account
def customerRegister(request):
    form = CustomerSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.is_customer = True
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("ccreate")
    context = {
        'form': form
    }
    return render(request, 'customer/signup.html', context)


# Customer Login
def customerLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("profile")
            else:
                return render(request, 'customer/login.html', {'error_message': 'Your account disable'})
        else:
            return render(request, 'customer/login.html', {'error_message': 'Invalid Login'})
    return render(request, 'customer/login.html')


# customer profile view
def customerProfile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    return render(request, 'customer/profile.html', {'user': user})


# Create customer profile
def createCustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("profile")
    context = {
        'form': form,
        'title': "Complete Your profile"
    }
    return render(request, 'customer/update_profile.html', context)


#  Update customer detail
def updateCustomer(request, id):
    form = CustomerForm(request.POST or None, instance=request.user.customer)
    if form.is_valid():
        form.save()
        return redirect('profile')
    context = {
        'form': form,
        'title': "Update Your profile"
    }
    return render(request, 'customer/update_profile.html', context)


def restRegister(request):
    form = RestaurantSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.is_restaurant = True
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("rcreate")
    context = {
        'form': form
    }
    return render(request, 'restaurant/signup.html', context)


# restuarant login
def restLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("rprofile")
            else:
                return render(request, 'restaurant/login.html', {'error_message': 'Your account disable'})
        else:
            return render(request, 'restaurant/login.html', {'error_message': 'Invalid Login'})
    return render(request, 'restaurant/login.html')


# restaurant profile view
def restaurantProfile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    return render(request, 'restaurant/profile.html', {'user': user})


# create restaurant detail
@login_required(login_url='/login/restaurant/')
def info(request):
    context = {
        'form': RestaurantForm(),
        'cm': Restaurant.objects.all(),
    }
    return render(request, 'restaurant/type.html', context)


@login_required(login_url='/login/restaurant/')
def info_save(request):
    cf = RestaurantForm(request.POST, request.FILES)
    if cf.is_valid():
        cf.save()
        return redirect('rcreate')


# Update restaurant detail
@login_required(login_url='/login/restaurant/')
def updateRestaurant(request, id):
    form = RestaurantForm(request.POST or None, request.FILES or None, instance=request.user.restaurant)
    if form.is_valid():
        form.save()
        return redirect('rprofile')
    context = {
        'form': form,
        'title': "Update Your Restaurant profile"
    }
    return render(request, 'restaurant/updateprofile.html', context)


# logout
def Logout(request):
    if request.user.is_restaurant:
        logout(request)
        return redirect("rlogin")
    else:
        logout(request)
        return redirect("login")


def foodie(request):
    context = {'form': foodForm(),
               'ff': Food.objects.all(),
               }
    return render(request, "restaurant/fooditems.html", context)


def orderlist(request):
    if request.POST:
        oid = request.POST['orderid']
        select = request.POST['orderstatus']
        select = int(select)
        order = Order.objects.filter(id=oid)
        if len(order):
            x = Order.ORDER_STATE_WAITING
            if select == 1:
                x = Order.ORDER_STATE_PLACED
            elif select == 2:
                x = Order.ORDER_STATE_ACKNOWLEDGED
            elif select == 3:
                x = Order.ORDER_STATE_COMPLETED
            elif select == 4:
                x = Order.ORDER_STATE_DISPATCHED
            elif select == 5:
                x = Order.ORDER_STATE_CANCELLED
            else:
                x = Order.ORDER_STATE_WAITING
            order[0].status = x
            order[0].save()

    orders = Order.objects.filter(restaurant=request.user.restaurant.id)
    corders = []

    for order in orders:

        user = User.objects.filter(id=order.orderedBy.id)
        user = user[0]
        corder = []
        if user.is_restaurant:
            corder.append(user.restaurant.rname)
            corder.append(user.restaurant.info)
        else:
            corder.append(user.customer.f_name)
            corder.append(user.customer.phone)
        items_list = orderItem.objects.filter(ord_id=order)

        items = []
        for item in items_list:
            citem = []
            citem.append(item.item_id)
            citem.append(item.quantity)
            menu = Food.objects.filter(id=item.item_id.id)
            citem.append(Food[0].price * item.quantity)
            menu = 0
            items.append(citem)

        corder.append(items)
        corder.append(order.total_amount)
        corder.append(order.id)

        x = order.status
        if x == Order.ORDER_STATE_WAITING:
            continue
        elif x == Order.ORDER_STATE_PLACED:
            x = 1
        elif x == Order.ORDER_STATE_ACKNOWLEDGED:
            x = 2
        elif x == Order.ORDER_STATE_COMPLETED:
            x = 3
        elif x == Order.ORDER_STATE_DISPATCHED:
            x = 4
        elif x == Order.ORDER_STATE_CANCELLED:
            x = 5
        else:
            continue

        corder.append(x)
        corder.append(order.delivery_addr)
        corders.append(corder)
        print(corders)

    context = {
        "orders": corders,
    }

    return render(request, "restaurant/order-list.html", context)


def food_save(request):
    ff = foodForm(request.POST, request.FILES)
    if ff.is_valid():
        ff.save()
        return render(request, "restaurant/thanks.html")


def order_history_user(request):
    user = request.user
    ordered_cust = None
    customers = Customer.objects.all()
    orders = []
    for cust in customers:
        if user.username == cust.user:
            ordered_cust = cust
    if ordered_cust != None:
        orders1 = OrderHistory.objects.filter(user_id__exact=ordered_cust.user_id).order_by('-order_timestamp')
        ordersNot = OrderHistory.objects.filter(user_id__exact=ordered_cust.user_id, status="Cancelled")
        for item in orders1:
            if item not in ordersNot:
                orders.append(item)
                print(orders)
    return render(request, 'customer/order_history_user.html', {'orders': orders, 'user': user})


def orderplaced(request):
    return render(request, 'orderplaced.html', {})
