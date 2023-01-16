from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude  = ('is_show',)

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control input-box','placeholder':'نام'}),
            'email' : forms.TextInput(attrs={'class':'form-control input-box','placeholder':'ایمیل'}),
            'body':forms.Textarea(attrs={'class':'form-control textarea-box','placeholder':'نظر شما'}),
        }