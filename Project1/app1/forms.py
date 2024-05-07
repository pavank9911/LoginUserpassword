# forms.py
from django import forms

class PatientFilterForm(forms.Form):
    query = forms.CharField(label='Search by Patient Name or ID', max_length=100)
