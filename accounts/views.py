from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth




# Create your views here.
def login(request):
    if request.method ==  'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid')
            return redirect('login')
    
    else:
        return render(request, 'login.html')

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
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name= firstname, last_name=lastname, )
                user.save()
                messages.info(request, 'user created')
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    request.session['visited_destinations'] = []
    return redirect('/')
