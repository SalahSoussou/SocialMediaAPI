from django.shortcuts import render ,HttpResponse ,redirect
from django.contrib.auth.models import User, auth

from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import  login_required

# Create your views here.
@login_required(login_url='signin')
def index(request):
    return render(request,'index.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordC = request.POST.get('passwordC')
        # print(username,password)
        # return HttpResponse('Signup Successful')
        if password == passwordC:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                # Create a new profile for the user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()

                # messages.info(request,'User created')
                return redirect('signup')
        else:
            messages.info(request,'Password not matching')
            return redirect('signup')
    else:
        return render(request,'signup.html')
    




# sigin logic
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('signin')
    else:
        return render(request,'signin.html')
    
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')