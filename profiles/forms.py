from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_postcode': 'Postal Code',
            'default_phone_number': 'Phone Number',
        }

        labels = {
           'default_full_name': 'Full Name',
           'default_email': 'Email Address',
           'default_phone_number': 'Phone Number',
           'default_postcode': 'Postal Code',
           'default_town_or_city': 'Town or City',
           'default_street_address1': 'Street Address line 1',
           'default_street_address2': 'Street Address line 2',
           'default_county': 'County',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].\
                widget.\
                attrs['class'] = 'border-black rounded-0 profile-form-imput'
            self.fields[field].label = labels[field]
