from django.shortcuts import render
from django.shortcuts import redirect
from . import models


def index(request):
    pass
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = 'Please enter both username and password!'
        if username.strip() and password:  # 确保用户名和密码都不为空
            try:
                user = models.User.objects.get(name=username)
            except:
                message = 'Wrong username or password！'
                return render(request, 'login/login.html', {'message': message})
            if user.password == password:
                return redirect('/index/')
            else:
                message = 'Wrong username or password！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')


def logout(request):
    pass
    return redirect("/login/")
