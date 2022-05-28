from django import forms
from .models import deba7
class AddDeba7Form(forms.ModelForm):


    class Meta:
        model = deba7
        fields = ('org','nom', 'prenom','limit')

class deba7edit(forms.ModelForm):
    class Meta:
        model = deba7
        fields = ('org','nom', 'prenom','limit')