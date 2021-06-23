from django.shortcuts import get_object_or_404, redirect, render
from .models import Signup
from django.utils import timezone
# Create your views here.

def home(req):
    people = Signup.objects.all()
    return render(req, 'home.html', {'people':people})


def new(req):
    return render(req, 'new.html')

def create(req):
    new_person = Signup()
    new_person.name = req.POST['name']
    new_person.age = req.POST['age']
    new_person.pub_date = timezone.now()
    new_person.email = req.POST['email']
    new_person.introduce = req.POST['introduce']
    new_person.save()
    return redirect('detail', str(new_person.id))

def detail(req, id):
    person = get_object_or_404(Signup, pk=id)
    return render(req, 'detail.html', {'person':person})

def edit(req, id):
    edit_person = get_object_or_404(Signup, pk=id)
    return render(req, 'edit.html', {'person':edit_person})

def update(req, id):
    update_person = get_object_or_404(Signup, pk=id)
    update_person.name = req.POST['name']
    update_person.age = req.POST['age']
    update_person.email = req.POST['email']
    update_person.introduce = req.POST['introduce']
    update_person.save()
    return redirect('detail', str(update_person.id))

def delete(req, id):
    delete_person = get_object_or_404(Signup, pk=id)
    delete_person.delete()
    return redirect('home')