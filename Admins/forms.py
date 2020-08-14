from django import forms
from foodapp.models import Place, SubCategory, Food_type
from django.core.validators import RegexValidator

alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets are allowed')


# Adding Places
class PlaceForm(forms.ModelForm):
    name = forms.CharField(label="Name", validators=[alpha])

    class Meta:
        model = Place
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label="Name", validators=[alpha])

    class Meta:
        model = SubCategory
        fields = '__all__'


class Food_typeForm(forms.ModelForm):
    class Meta:
        model = Food_type
        fields = '__all__'
