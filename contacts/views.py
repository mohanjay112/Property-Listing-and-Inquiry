from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        
    #    if request.user.is_authenticated:
    #        user_id = request.user.id
    #        has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
    #        if has_contacted:
    #            messages.error(request, 'you have already made an inqury for this listing')
    #            return redirect('/listings/'+listing_id)    
              
                          
                
        
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        
        contact.save()
        
        send_mail(
            'Property Listing Inquiry',
            'There is been an inquiry for ' + listing + '.Sign into the admin panel for more info',
            'settings.EMAIL_HOST_USER',
            ['mohanjay113@gmail.com','royaljay.ak47@gmail.com'],
            fail_silently=False
            
        )
        
        #send email
        
        
        
        messages.success(request, 'your request has been submitted,  a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)

