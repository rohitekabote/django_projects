from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['psw-repeat']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user already exist")
            elif User.objects.filter(emial=email).exists():
                messages.info(request, "email already taken")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name= firstname, last_name=lastname, )
                user.save()
                print('user created')
        else:
            print("password not matching")
        return redirect('/')
    return render(request, 'register.html')
