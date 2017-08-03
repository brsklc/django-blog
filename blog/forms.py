from django import forms
from .models import Comment

class YorumForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)