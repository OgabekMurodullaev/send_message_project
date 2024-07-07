from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Contact


# Create your views here.
class ContactMessageCreateView(CreateView):
    model = Contact
    template_name = 'xabar_yozish.html'
    fields = ['firstname', 'lastname', 'sender', 'phone', 'message']

class ContactsMessagesView(ListView):
    model = Contact
    template_name = 'xabarlar.html'
