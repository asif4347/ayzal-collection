from django import forms
from .models import *


class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = '__all__'


class ContactsForm(forms.ModelForm):
    # subscribe = forms.CheckboxInput()

    class Meta:
        model = Contacts
        fields = '__all__'
