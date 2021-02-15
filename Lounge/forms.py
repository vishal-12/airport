# -*- coding: utf-8 -*-
from django import forms
from Lounge.models import AirpotLoungeModel


class LoungeProjectsFrom(forms.ModelForm):
    class Meta:
        model = AirpotLoungeModel
        exclude = []

    name = forms.CharField(label='Airpot Lounge')
    price = forms.CharField(label='Price of Airpot Lounge')
    size = forms.CharField(label='Size of Airpot Lounge')