from email.headerregistry import Address
from django.db import models
from accounts.models import Account
from debah.models import deba7
import json
from django.core.validators import MaxValueValidator, MinValueValidator
file = open('request/wilayas.json',encoding="utf8")
data = json.load(file)
choix = []
choix_b = ['',[]]
for i in data:
	choix.append((i['name']))
	for j in i['dairats']:
		if 'baladyiats' in j:
			for k in j['baladyiats']:
				choix_b.append((i['name'],k['name']))
				#print((k['name']))
class request_s(models.Model):
	owner 		= models.OneToOneField(Account , on_delete=models.CASCADE)
	wilaya		= models.CharField(max_length=100)
	Address	    = models.CharField(max_length=100)
	taken       = models.BooleanField(default=False)
	
	# Create your models here.
 
class date_request(models.Model):
	organisation = models.ForeignKey(Account , on_delete=models.CASCADE , related_name="organisation",limit_choices_to={'is_org': True})
	debah		 = models.ForeignKey(deba7 , on_delete=models.CASCADE , related_name="debah")
	simple_user  = models.ForeignKey(Account , on_delete=models.CASCADE , related_name="simple_user" ,limit_choices_to={'is_org': False})
	jour         = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(2)])
	date 		 = models.TimeField(blank=True , null=True)
	# deba7
	# org
		#user
		 #date
		  # 

