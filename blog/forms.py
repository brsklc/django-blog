from django import forms
from .models import Comment

class YorumForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content','user_name')
        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'cols':38, 'placeholder':'yorum',}),
            'user_name': forms.TextInput(attrs={'placeholder':'isim',}),
        }