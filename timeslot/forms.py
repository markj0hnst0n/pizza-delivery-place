from django import forms
from .models import Timeslot


class TimeslotForm(forms.ModelForm):

    class Meta:
        model = Timeslot
        fields = '__all__'

    start_time = forms.TimeInput()
    end_time = forms.TimeInput()
