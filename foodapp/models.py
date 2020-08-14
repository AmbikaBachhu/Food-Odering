from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=20, blank=False)
    l_name = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=40, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    address = models.TextField()

    def __str__(self):
        return self.user.username or ''


class Place(models.Model):
    id = models.IntegerField(primary_key=True, default=None, blank=True, )
    name = models.CharField(max_length=50, null=True, default=None, blank=True)

    def __str__(self):
        return self.name or ''


class SubCategory(models.Model):
    id = models.IntegerField(primary_key=True, default=None, blank=True, )
    name = models.CharField(max_length=50, null=True, default=None, blank=True)

    def __str__(self):
        return self.name or ''


class Restaurant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rname = models.CharField(max_length=100, blank=False)
    min_ord = models.CharField(max_length=5, blank=False)
    location = models.CharField(max_length=40, blank=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE,default="")
    subcat = models.ManyToManyField(SubCategory, default="")
    price = models.IntegerField(blank=False,default=0)
    delivery = models.IntegerField(default=0)
    menupic = models.ImageField(upload_to='images/', null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

    STARS = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'),)
    votes = models.IntegerField(choices=STARS, default=4)
    REST_STATE_OPEN = "Open"
    REST_STATE_CLOSE = "Closed"
    REST_STATE_CHOICES = (
        (REST_STATE_OPEN, REST_STATE_OPEN),
        (REST_STATE_CLOSE, REST_STATE_CLOSE)
    )
    status = models.CharField(max_length=50, choices=REST_STATE_CHOICES, default=REST_STATE_OPEN, blank=False)
    approved = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.rname or ''


class Food_type(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.title or ''

    @property
    def get_food(self):
        return Food.objects.filter(categories__title=self.title)


class Food(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    rest = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    food_type = models.ForeignKey(Food_type, null=True, on_delete=models.CASCADE)
    digital = models.BooleanField(default=False, null=True, blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total_amount = models.IntegerField(default=0)
    door_no = models.CharField(max_length=200, blank=True)
    landmark = models.CharField(max_length=200, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,null=True)
    complete = models.BooleanField(default=False)

    ORDER_STATE_WAITING = "Waiting"
    ORDER_STATE_PLACED = "Placed"
    ORDER_STATE_ACKNOWLEDGED = "Accepted by Restaurant"
    ORDER_STATE_COMPLETED = "Cooking"
    ORDER_STATE_CANCELLED = "Cancelled"
    ORDER_STATE_DISPATCHED = "Delivered"

    ORDER_STATE_CHOICES = (
        (ORDER_STATE_WAITING, ORDER_STATE_WAITING),
        (ORDER_STATE_PLACED, ORDER_STATE_PLACED),
        (ORDER_STATE_ACKNOWLEDGED, ORDER_STATE_ACKNOWLEDGED),
        (ORDER_STATE_COMPLETED, ORDER_STATE_COMPLETED),
        (ORDER_STATE_CANCELLED, ORDER_STATE_CANCELLED),
        (ORDER_STATE_DISPATCHED, ORDER_STATE_DISPATCHED)
    )
    status = models.CharField(max_length=50, choices=ORDER_STATE_CHOICES, default=ORDER_STATE_WAITING)

    def __str__(self):
        return str(self.id) + ' ' + self.status

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class Addresss(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    door_no = models.CharField(max_length=200, null=False)
    landmark = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.landmark or ''


class OrderItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.food.price * self.quantity
        return total


class OrderHistory(models.Model):
    food = models.ForeignKey(Food, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    user = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    rest = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=True)
    order_timestamp = models.DateTimeField(null=True)

    @property
    def get_total(self):
        total = self.food.price * self.quantity
        return total
