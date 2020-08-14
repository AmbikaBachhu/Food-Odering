from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import CharField

from foodapp.models import User, Customer, Restaurant, Food


class CustomerSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_customer = True
            if commit:
                user.save()
            return user


class RestaurantSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_restaurant = True
            if commit:
                user.save()
            return user


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['f_name', 'l_name', 'city', 'phone', 'address']


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"


class foodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"
