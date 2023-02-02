from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import profile


def index(request):
    return render(request,'index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email taken')
                return redirect( 'signup')
            elif User.objects.filter(username = username).exists(): 
                messages.info(request,'Username taken')
                return redirect( 'signup')
            else:
                user = User.objects.create_user(username=username,email = email, password=password)
                user.save()

                #log user in and direct to settings
                #create a profile object for the new guy
                user_model = User.objects.get(username = username)
                new_profile = profile.objects.create(user = user_model, id_user = user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request,'パスワードが間違っています')
            return redirect('signup')


    else:
        return render(request,'signup.html')

    





