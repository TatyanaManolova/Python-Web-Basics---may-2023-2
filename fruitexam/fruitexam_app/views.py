from django.shortcuts import render, redirect

from fruitexam.fruitexam_app.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, FruitDeleteForm, \
    FruitCreateForm, FruitEditForm
from fruitexam.fruitexam_app.models import ProfileModel, FruitModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def get_fruit(pk):
    fruit = FruitModel.objects.filter(pk=pk).get()
    return fruit


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'base/index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = sorted(FruitModel.objects.all(), key=lambda x: x.pk)

    context = {
        'fruits': fruits,
        'fruits_len': len(fruits),
        'profile': profile
    }
    return render(request, 'base/dashboard.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    fruits = FruitModel.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    fruits = FruitModel.objects.all()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        for fruit in fruits:
            fruits_form = FruitDeleteForm(request.POST, instance=fruits)
            fruits_form.save()

        return redirect('index')

    context = {
        'profile': profile
    }

    return render(request, 'profile/delete-profile.html', context)


def create_fruit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, pk):
    fruit = get_fruit(pk)
    profile = get_profile()

    context = {
        'fruit': fruit,
        'profile': profile
    }

    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruit/delete-fruit.html', context)
