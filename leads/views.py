from django.shortcuts import render
from .models import Lead


def index(request):
    leads = Lead.objects.all()
    
    context = {
        'leads':leads,
    }


    return render(request, 'leads/index.html', context)
    
