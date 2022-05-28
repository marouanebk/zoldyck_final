import re
from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone
from accounts.models import Account
from request.models import request_s
from django.urls import reverse
from .models import deba7
from .forms import AddDeba7Form , deba7edit
from request.models import date_request
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from notifications.models import Notification


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
import threading


def list_abt(request):
    user=request.user
    list = deba7.objects.filter(org=user.id)
    return render(request, 'org/yourabatt.html',{'list':list})


def add_deba7(request):
    print('ok')
    if request.method == 'POST':
        form = AddDeba7Form(request.POST)
        print('ok1')
        if form.is_valid():
            print('ok2')
            form.save()
    form = AddDeba7Form()
    return render(request, 'deba7s/add_deba7.html', {'form': form})

def edit(request, abt_id):
    instance = deba7()
    if abt_id:
        instance = get_object_or_404(deba7 , pk=abt_id)
    else :
        instance = deba7()
    
    form = deba7edit(request.POST or None, instance=instance)

    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('account:home'))
    return render(request, 'deba7s/edit.html', {'form': form})

def delete(request, abt_id):
    deba7.objects.filter(pk=abt_id).delete()

    return HttpResponseRedirect(reverse('account:home'))




def association_org(request,req_id):
    list_d = deba7.objects.filter(org=request.user,limit_reacher=False)
    page = request.GET.get('page')
    p = Paginator(list_d,2)
    if request.POST:
        butcher = request.POST.get("butcher")
        print(butcher)
        req = get_object_or_404(request_s,pk=req_id)
        if butcher is not None:
            req.taken = True
            req.save()
            simple_user = req.owner
            deba7_user =get_object_or_404(deba7,pk=int(butcher))
            deba7_user.taken = deba7_user.taken + 1
            if deba7_user.taken == deba7_user.limit:
                deba7_user.limit_reacher = True
            deba7_user.save()
            acc = date_request.objects.create(organisation=request.user,debah=get_object_or_404(deba7,pk=int(butcher)),simple_user=req.owner,date=timezone.now())
            nott = Notification.objects.create(from_user=request.user,to_user=req.owner,date=timezone.now())
            acc.save()
            print('yh')
            try:
                send_email(simple_user,request, deba7_user)
            except:
                print("email not sent")
            return redirect("request:all_request")
    try:
        list_d = p.get_page(page)
    except PageNotAnInteger:
        list_d = p.get_page(page)
    except EmptyPage:
        list_d = p.page(p.num_pages)
    return render(request, "org/listofabatt.html" , {'list_d':list_d}) 



class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_email(user, request  , deba7 ):
    current_site = get_current_site(request)
    email_subject = 'Eid Adha'
    email_body = render_to_string('deba7s/email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'deba7': deba7,
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    # if not settings.TESTING:
    EmailThread(email).start()

