from xml.dom import ValidationErr
from django import forms
from .models import Cashbook, Comment, Hashtag
from django.core.exceptions import ValidationError


class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = ['title', 'content', 'detail', 'image', 'hashtags']

    def __init__(self, *args, **kwargs):
        super(CashbookForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False       
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['content'].widget.attrs['readonly'] = True


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']