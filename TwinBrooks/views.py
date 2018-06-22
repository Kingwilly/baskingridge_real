from django.contrib import messages
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from .forms import ContactForm
from BaskingRidgeFiles.models import news_entry

# from TwinBrooks.settings import FRONT_END_CONTACTFORM_EMAIL, FRONTEND_PRO_EMAIL
from BaskingRidgeFiles.models import menu_entry, gallery_image

'''
Static Views that serve as the frontend content.
'''
def home_static(request):
    news = news_entry.objects.all().first()
    return render(request,
                  './b_ridge/pages/index.html',
                  {'home_active': True, 'news_entry': news})

def rest_static(request):
    return render(request,
                  './b_ridge/pages/rest.html',
                  {'restaurant_active': True})

def menus_static(request):
    wedding_menus = menu_entry.objects.all().order_by('my_order').filter(menu_type='Wedding')
    social_menus = menu_entry.objects.all().filter(menu_type='Social Events').order_by('my_order')
    sweet_menus = menu_entry.objects.all().filter(menu_type='Sweet Sixteens').order_by('my_order')
    corporate_menus = menu_entry.objects.all().filter(menu_type='Corporate').order_by('my_order')
    print wedding_menus
    return render(request,
                  './b_ridge/pages/menus.html',
                  {
                      'menus_active': True,
                      'wedding_menus': wedding_menus,
                      'social_menus': social_menus,
                      'sweet_menus': sweet_menus,
                      'corporate_menus': corporate_menus,
                    }
                    )

def gallery_static(request):
    gallery_items = gallery_image.objects.all()
    return render(request,
                  './b_ridge/pages/gallery.html',
                  {'gallery_active': True, 'gallery_items': gallery_items})


def vendors_static(request):
    return render(request,
                  './b_ridge/pages/vendors.html',
                  {'vendors_active': True})

def wedding_promo_static(request):
    return render(request,
                  './b_ridge/pages/wedding_promo.html',
                  {'celebrate_active': True})


def contact_static(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print 'form valid'
            data = form.cleaned_data
            name = data['name']
            email = data['email']
            event_type = data['event_type']
            event_date = data['event_date']
            phone_number = data['phone_number']
            message = data['body']
            plain_message = (
                'Hello, \n  \n There was a new form entry: \n \n')
            # Include a html template:
            text_content = plain_message + name + '\n Phone Number: ' + \
                phone_number + '\n Email: ' + email +   '\n Event Type: ' + event_type +  '\n Event Date: ' + event_date + '\n Message: ' + message + '\n - Basking Ridge Form Mail Bot'
            msg = EmailMultiAlternatives(
                subject="Basking Ridge Contact Form",
                body=text_content,
                to=['info@baskingridgecatering.com', 'adam@builtbykingwilly.com', 'zacharybedrosian@gmail.com', 'racquaviva@aol.com'],

            )
            # Optional Anymail extensions:
            msg.track_clicks = True
            msg.tags = ["Member Inquiry"]
            messages.success(
            request, 'Thanks! We will get in touch soon.')
            # Send it:d
            msg.send()
            return redirect("thankyou_static")
    return render(request,
               './b_ridge/pages/contact.html',
                  {'contact_active': True, 'form': form})

def thankyou_static(request):
    return render(request,
                  './b_ridge/pages/thankyou.html',
                  {'contact_active': True,})

def events_static(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            email = data['email']
            phone_number = data['phone_number']
            handicap = data['handicap']
            message = data['body']
            plain_message = (
                'Hello, \n  \n There was a new member inquiry on the site.: \n \n')
            # Include a html template:
            text_content = plain_message + name + '\n Phonenumber: ' + \
                phone_number + '\n Email: ' + email + '\n Handicap: ' + \
                handicap + '\n Message: ' + message + '\n - WVGC Mail Bot'
            msg = EmailMultiAlternatives(
                subject="WCGC Membership Inquiry",
                body=text_content,
                from_email="WVGC Admin <no-reply@watchungvalleygc.com>",
                to=[FRONT_END_CONTACTFORM_EMAIL],

            )
            # Optional Anymail extensions:
            msg.track_clicks = True
            msg.tags = ["Member Inquiry"]
            # Send it:d
            msg.send()
            messages.success(request, 'Request successfully sent.')
            return redirect("thankyou_static")
    return render(request,
                  './front-end/pages/events.html',
                  {'events_active': True, 'form': form})

