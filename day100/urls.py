from django.conf.urls import url
from django.contrib import admin
from app888 import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login, name="login"),
    url(r'^register/', views.register, name="register"),
    url(r'^$', views.index, name="index"),

    url(r'^show/', views.show, name="show"),
    url(r'^edit/(\d+)', views.edit, name="edit"),
    url(r'^drop/(\d+)', views.drop, name="drop"),
]
