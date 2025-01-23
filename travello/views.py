from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    
    # dect1 = Destination()
    # dect1.name = "MUMBAI"
    # dect1.des = "A financial center, it's India's largest city."
    # dect1.img = 'destination_1.jpg'
    # dect1.price = 700
    # dect1.offer = False
    
    # dect2 = Destination()
    # dect2.name = "Bengaluru"
    # dect2.des = "The center of India's high-tech industry"
    # dect2.img = 'destination_2.jpg'
    # dect2.price = 800
    # dect2.offer = True
    
    # dect3 = Destination()
    # dect3.name = "Pune"
    # dect3.des = "Pune is a sprawling city in the western Indian state of Maharashtra."
    # dect3.img = 'destination_3.jpg'
    # dect3.price = 750
    # dect3.offer = False
    
    # dects = [dect1, dect2, dect3]
    
    dects = Destination.objects.all()
    
    return render(request, 'index.html', {'dects' : dects})