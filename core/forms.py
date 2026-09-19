from django import forms
from django.db.transaction import clean_savepoints

from .models import contact
class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields={"name","l_name","email","content","message"}
