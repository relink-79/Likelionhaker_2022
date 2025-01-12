from django.shortcuts import get_object_or_404, redirect, render
from .models import Signup
from django.utils import timezone
import threading
# Create your views here.

def home(req):
    people = Signup.objects.all()
    return render(req, 'home.html', {'people':people})


def new(req):
    return render(req, 'new.html')

def timer(req) :
    return render(req, 'timer.html')


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
def abcd(req):
    Acode_req = req.GET['Acode']
    Bcode_req = req.GET['Bcode']
    result = 'result'
    deresult = 'deresult'
    Acode_de = Acode_req.replace(" ","")
    Bcode_de = Bcode_req.replace(" ","")
    if Acode_req == Bcode_req:
        result = 'true'
    else:
        result = 'false'
    if Acode_de == Bcode_de:
        deresult = 'true'
    else:
        deresult = 'false'
    return render(req,'abcd.html',{'Fcode':Acode_req,'Scode':Bcode_req,'result':result,'deresult':deresult})
def abc(req):
    return render(req,'abc.html')
def wisesaying(req):
    return render(req,'wisesaying.html')
def display(req):
    display_req=req.GET['wisesaying']
    return render(req,'display.html',{'display':display_req})
    
