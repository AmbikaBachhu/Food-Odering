import json
from foodapp.models import *


def cookiecart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print(cart)
    items = []
    order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            food = Food.objects.get(id=i)
            total = (food.price * cart[i]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            item = {
                'food': {
                    'id': food.id,
                    'name': food.name,
                    'price': food.price,
                    'imageURL': food.imageURL,
                },
                'quantity': cart[i]['quantity'],
                ' get_total': total
            }
            items.append(item)
            if food.digital == False:
                order['shipping'] = True
        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        cookieDate = cookiecart(request)
        cartItems = cookieDate['cartItems']
        order = cookieDate['order']
        items = cookieDate['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        food = Food.objects.get(id=item['food']['id'])
        orderItem = OrderItem.objects.create(
            food=food,
            order=order,
            quantity=item['quantity'],
        )
    return customer, order
