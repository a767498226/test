from django.shortcuts import render, HttpResponse, redirect

from app888 import models
from app888.forms import RegForm


def wrapper(func):
    def inner(request, *args, **kwargs):
        if request.session.get("is_login"):
            ret = func(request, *args, **kwargs)
            return ret
        else:
            return redirect("login")
    return inner


@wrapper
def index(request):
    return render(request, "index.html")


@wrapper
def register(request):

    form_obj = RegForm()
    action = "注册"
    if request.method == "POST":
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("index")

    return render(request, "register.html", {"form_obj": form_obj, "action":action})


def login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        auth = models.UserInfo.objects.filter(username=username, password=password).exists()
        if auth:
            request.session["is_login"] = "ok"
            return redirect("show")
        else:
            return redirect("login")

    return render(request, "login.html")


@wrapper
def show(request):

    all_user = models.UserInfo.objects.all()

    return render(request, "show.html", {"all_user": all_user})



@wrapper
def edit(request, id):
    action = "编辑"
    obj = models.UserInfo.objects.filter(pk=id).first()
    form_obj = RegForm(instance=obj)
    if request.method == "POST":
        form_obj = RegForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("show")

    return render(request, "register.html", {"form_obj": form_obj, "action": action})


@wrapper
def drop(request,id):
    models.UserInfo.objects.filter(pk=id).delete()
    return redirect("show")

