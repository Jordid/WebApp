from django import forms
from django.forms import ModelForm
from models import *

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
    