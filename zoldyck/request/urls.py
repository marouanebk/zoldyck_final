from django.urls import include, re_path,path
from . import views


app_name = 'request'
urlpatterns = [
    path("request/", views.request_v , name="request_v"),
    path("all_request/", views.all_request , name="all_request"),
    path("confirm/", views.confirm_request , name="confirm"),

]
