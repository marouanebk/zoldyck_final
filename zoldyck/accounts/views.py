from django.shortcuts import render
from django.shortcuts import redirect
from accounts.models import Account
from django.http import HttpResponse
from .forms import RegistrationForm , AccountAuthenticationForm , request_form
from django.contrib.auth import login, authenticate, logout






def home(request):
    return render(request, 'account/index.html')
    # Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/')


# def signup(request):
#     context = {'form':RegistrationForm}
#     return render(request, 'account/signup.html', context)


def signup(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('account:home')
        else:
            context['form'] = form


    else:
        form = RegistrationForm()
        context['form'] = form
    return render(request, 'account/signup.html', context)

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated: 
        return redirect("account:home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            print("form is valid")

            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("account:home")
        else:
            print("form isnt valid")

    else:
        form = AccountAuthenticationForm()
        print("form isnt request psot")
    context['login_form'] = form

    # print(form)
    return render(request, "account/signin.html", context)

def org_sign(request):
    if request.POST:
        form = request_form(request.POST,initial={'is_org':True,'is_active':False})
        if form.is_valid():
            print("valid")
            form.is_active=False
            form.is_org=True
            instance = form.save(commit=False)
            instance.is_active=False
            instance.is_org=True
            instance.save()
            return redirect("account:home")
        else:
            print(form.errors.as_data)
    else:
        form = request_form

    return render(request, "orgsign.html", {'form':form})

def pro(request):
    return render(request, "account/pro.html")

def all_org(request):
    orgs = Account.objects.filter(is_org=True)
    return render (request, "pageorgs.html",{'orgs':orgs})