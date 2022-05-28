from django.contrib import admin

from .models import Account
from request.models import request_s

from request.models import date_request
admin.site.register(date_request)
admin.site.register(Account)
admin.site.register(request_s)