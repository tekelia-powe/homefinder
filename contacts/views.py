from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        landlord_email = request.POST['landlord_email']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, " YOu have already made an inquiry for this listing. ")
                print('repeat')
                return redirect('/listings/'+listing_id)

        contact = Contacts(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id,)
        contact.save()
        print('saved')

        send_mail(
            'Property Inquiry',
            'There has been an inquiry for '+listing+'. Sign into your admin panel for more information',
            'tekeliap@gmail.com', [landlord_email],
            fail_silently=False,
        )
        print('ok')
        messages.success(request, "Your request has been submitted, the landlord will get back with you soon. ")
        return redirect('/listings/'+listing_id)