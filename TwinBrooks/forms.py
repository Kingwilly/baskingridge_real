from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):

    name = forms.CharField(max_length=100,
                           label=_(u'Your Full Name'), required=True)
    phone_number = forms.CharField(max_length=100,
                           label=_(u'Your Phone Number'), required=True)
    email = forms.EmailField(max_length=200,
                             label=_(u'Your Email Address'), required=True)
    event_type = forms.CharField(max_length=200,
                             label=_(u'Your Event Type'), required=True)
    event_date = forms.CharField(max_length=200,
                             label=_(u'Your Event Date'), required=True)
    body = forms.CharField(required=False, widget=forms.Textarea,
                           label=_(u'Your Message'))

    def __init__(self, data=None, files=None, request=None,
                 recipient_list=None, *args, **kwargs):
        self.request = request
        if recipient_list is not None:
            self.recipient_list = recipient_list
        super(ContactForm, self).__init__(data=data, files=files,
                                          *args, **kwargs)
