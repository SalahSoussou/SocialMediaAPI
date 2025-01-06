from django.shortcuts import render ,HttpResponse ,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
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
                # messages.info(request,'User created')
                # return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('signup')
    else:
        return render(request,'signup.html')