from .import models
from django import forms



class MemeForm(forms.ModelForm):
    class Meta:
        model = models.Meme
        fields = ('meme_owner', 'caption','url')