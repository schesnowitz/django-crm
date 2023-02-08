from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

def landing_page(request):
    return render(request, 'landing.html')

def index(request):
    leads = Lead.objects.all()  
    context = {
        'leads': leads
    }
    return render(request, 'leads/index.html', context)
    
def detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, 'leads/detail.html', context)
# Basic form
# def create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         print('getting a post request')
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print('form is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             print("lead created")
#             return redirect('leads/') 
#     context = {
#         'form': form
#     }   
#     # lead = Lead.objects.create()
#     return render(request, 'leads/create.html', context)

def create(request):
    form = LeadModelForm()
    if request.method == "POST":
        # print('getting a post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index) 
    context = {
        'form': form

    }   
    # lead = Lead.objects.create()
    return render(request, 'leads/create.html', context)


def update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":

        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect(index) 
    context = {
        'lead': lead,
        'form': form
    }
    return render(request, 'leads/update.html', context)

def delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect(index) 
