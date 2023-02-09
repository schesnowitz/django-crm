from django.shortcuts import (render, redirect, reverse) 
# from django.urls import 
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
    CreateView
    ) 


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login') 

class LandingView(TemplateView):
    template_name = 'landing.html'


class IndexView(ListView):
    template_name = 'leads/index.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'
    # default is object_list


class LeadDetailView(DetailView):
    template_name = 'leads/detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(CreateView):
    template_name = 'leads/create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:index') 


class LeadUpdateView(UpdateView):
    template_name = 'leads/update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:index')


class LeadDeleteView(DeleteView):
    template_name = 'leads/delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:index')
