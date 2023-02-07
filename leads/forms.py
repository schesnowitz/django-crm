from django import forms
from .models import Lead

class LeadForm(forms.Form):
    first_name      = forms.CharField()
    last_name       = forms.CharField()
    age             = forms.IntegerField()
    # agent           = forms.ForeignKey()

    


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',     
            'last_name',       
            'age',             
            'agent',           

        )

    

