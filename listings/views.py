from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import rent_choices, bedroom_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    
    return render(request,'listings/listings.html', context)
    
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request,'listings/listing.html', context)

def search(request):
    queryset_lists = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_lists = queryset_lists.filter(description__icontains=keywords)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_lists = queryset_lists.filter(
                city__iexact=city)
    
    if 'rent' in request.GET:
        rent = request.GET['rent']
        if rent:
            queryset_lists = queryset_lists.filter(
                rent__lte=rent)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_lists = queryset_lists.filter(
                bedrooms__lte=bedrooms)
    
    context = {
        
        'rent_choices': rent_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_lists,
        'values': request.GET
    }
    return render(request,'listings/search.html', context)
