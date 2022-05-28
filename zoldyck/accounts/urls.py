from django.urls import include, re_path,path
from . import views


app_name = 'account'
urlpatterns = [
    path("", views.home , name="home"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.login_view, name="signin"),
    path("logout/", views.logout_view , name="logout"),
    path("joinus/", views.org_sign, name="join us"),
    path("pro/" ,   views.pro, name="pro"),
    path("donate/", views.all_org, name="all_org"),

]
