from django import forms

from .models import Snippets

class AddSnippet(forms.ModelForm):

    class Meta:
        model = Snippets
        fields = ('title','language', 'description', 'snippet',)