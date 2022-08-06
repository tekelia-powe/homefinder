from django.shortcuts import render
from django.http import HttpResponse

from listings.choices import rent_choices, bedroom_choices
from listings.models import Listing
from landlords.models import Landlord

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]

    context = {
        'listings' : listings,
        'rent_choices': rent_choices,
        'bedroom_choices': bedroom_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    landlords = Landlord.objects.order_by('-hire_date')
    #featured landlord
    mvp_landlord = Landlord.objects.all().filter(is_mvp=True)
    context = {
        'landlords': landlords,
        'mvp_landlord': mvp_landlord
    }

    return render(request, 'pages/about.html', context)