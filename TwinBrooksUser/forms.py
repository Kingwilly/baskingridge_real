from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class MemberFormPersonal(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'gender',
            'first_name',
            'middle_name',
            'last_name',
            'phone_numner',
            'e_contact_full_name',
            'e_contact_phone_number',
            'email',
            'suffix',

        ]

    def __init__(self, *args, **kwargs):
        super(MemberFormPersonal, self).__init__(*args, **kwargs)
        self.fields['middle_name'].widget.attrs\
            .update({
                'placeholder': 'Middle Name',
                'class': 'input-calss_name'
            })
        self.fields['phone_numner'].widget.attrs\
            .update({
                'placeholder': 'Ex: (908) 123 9824',
                'class': 'input-calss_name'
            })
        self.fields['e_contact_full_name'].widget.attrs\
            .update({
                'placeholder': 'John Smith',
                'class': 'input-calss_name'
            })
        self.fields['e_contact_phone_number'].widget.attrs\
            .update({
                'placeholder': 'Ex: (908) 123 9824',
                'class': 'input-calss_name'
            })


class MemberProfilePhotoForm(forms.ModelForm):
    image_errors = {
        'required': 'Please upload a profile image.',
    }

    profile_image = forms.ImageField(
        label='Select An Image',
        error_messages=image_errors

    )

    class Meta:
        model = User
        fields = [
            'profile_image',

        ]

    def __init__(self, *args, **kwargs):
        super(MemberProfilePhotoForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True
