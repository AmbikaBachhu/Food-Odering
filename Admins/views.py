from django.shortcuts import render, redirect
from foodapp.models import Place, SubCategory, Food_type

# Create your views here.
from Admins.forms import PlaceForm, CategoryForm, Food_typeForm
from django.contrib import messages


# Create your views here.
def all(request):
    return render(request, "Admins/all.html")


def place(request):
    messages.success(request, "New place Added")
    return render(request, "Admins/place.html", {"place": PlaceForm()})


def saveplace(request):
    idno = request.POST.get("id")
    name = request.POST.get("name")
    Place(id=idno, name=name).save()
    messages.success(request, "saved")
    return redirect('place')


def viewplace(request):
    places = Place.objects.all()
    return render(request, "Admins/view_places.html", {"places": places})


def updateplace(request):
    no = request.GET.get("mn")
    up = Place.objects.get(id=no)
    return render(request, "Admins/update_places.html", {"up": up})


def saveupdate(request):
    no = request.POST.get("id")
    name = request.POST.get("name")
    Place.objects.filter(id=no).update(name=name)
    return redirect('view_place')


def deleteplace(request):
    no = request.GET.get("kl")
    de = Place.objects.get(id=no).delete()
    return redirect('view_place')


def cat(request):
    messages.success(request, "New category Added")
    return render(request, "Admins/category.html", {"cats": CategoryForm()})


def savecategory(request):
    idno = request.POST.get("id")
    name = request.POST.get("name")
    SubCategory(id=idno, name=name).save()
    messages.success(request, "saved")
    return redirect('cat')


def viewcategory(request):
    cats = SubCategory.objects.all()
    return render(request, "Admins/view_category.html", {"category": cats})


def updatecategory(request):
    no = request.GET.get("mn")
    up = SubCategory.objects.get(id=no)
    return render(request, "Admins/update_category.html", {"up": up})


def saveupcat(request):
    no = request.POST.get("id")
    name = request.POST.get("name")
    SubCategory.objects.filter(id=no).update(sub=name)
    return redirect('view_category')


def deletecategory(request):
    no = request.GET.get("kl")
    de = SubCategory.objects.get(id=no).delete()
    return redirect('view_category')


def food_type(request):
    messages.success(request, "New Type of food Added")
    return render(request, "Admins/food_type.html", {"food_type": Food_typeForm()})


def save_foodtype(request):
    ff = Food_typeForm(request.POST)
    if ff.is_valid():
        ff.save()
        return redirect('food_type')


def view_foodtype(request):
    foods = Food_type.objects.all()
    return render(request, "Admins/view_foodtype.html", {"foods": foods})

def updatefood_type(request):
    no = request.GET.get("mn")
    up = Food_type.objects.get(id=no)
    return render(request, "Admins/update_foodtype.html", {"up": up})


def saveupftype(request):
    no = request.POST.get("id")
    title = request.POST.get("tile")
    Food_type.objects.filter(id=no).update(title=title)
    return redirect('view_foodtype')


def deletefood_type(request):
    no = request.GET.get("kl")
    de = Food_type.objects.get(id=no).delete()
    return redirect('view_foodtype')