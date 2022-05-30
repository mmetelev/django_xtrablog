from django.shortcuts import render

from .models import *
from .forms import ContactForm


def show_about(request):
    abouts = About.objects.all()
    teams = Team.objects.all()
    cards = Card.objects.all()
    context = {
        'contacts': abouts,
        'teams': teams,
        'cards': cards,
    }
    return render(request, 'contact/about.html', context=context)


def show_contact(request):
    contacts = Contact.objects.all()
    abouts = About.objects.all()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
        'contact': contacts,
        'abouts': abouts,

    }

    return render(request, 'contact/contact.html', context=context)
