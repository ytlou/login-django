from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == "123":
        return redirect("http://www.ece.rutgers.edu/")

    return render(request, 'login.html', {"error_msg": "user name or password is wrong"})