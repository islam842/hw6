from django import forms
from . import models


class ShowForm(forms.ModelForm):
    class Meta:
        model = models.Phones
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'