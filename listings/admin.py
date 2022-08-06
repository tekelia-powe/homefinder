from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','rent','deposit', 'list_date','landlord')
    list_display_links = ('id', 'title')
    list_filter = ['landlord',]
    list_editable = [('is_published')]
    search_fields =('title', 'description', 'address', 'city', 'zip', 'rent')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
