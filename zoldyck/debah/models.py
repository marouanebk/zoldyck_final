from django.db import models
from accounts.models import Account
# Create your models here.
class deba7(models.Model):
    org = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='org',limit_choices_to={'is_org':True})
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    phone_number = models.IntegerField(blank=True , null=True)
    limit = models.IntegerField()
    taken = models.IntegerField(default=0)
    location = models.CharField(max_length=100 , null=True , blank=True)
    limit_reacher = models.BooleanField(default=False)

    def __str__(self):
        return self.nom+" "+self.prenom+"                             org : "+self.org.first_name
