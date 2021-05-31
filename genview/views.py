from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact

class ContactList(ListView): 

    model = Contact
    template_name ='contact_list.html'

class ContactDetail(DetailView): 

    model = Contact
    template_name ='contact_detail.html'
# Create your views here.
class ContactCreate(CreateView): 
    model = Contact
    template_name ='contact_form.html'
    fields = '__all__'

class ContactUpdate(UpdateView): 

    model = Contact
    template_name ='contact_form.html'

class ContactDelete(DeleteView): 

    model = Contact
    template_name ='contact_confirm_delete.html'
