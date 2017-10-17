from django import forms
from .models import *

class GoodForm(forms.ModelForm):
    preifx = 'comment_form'
    class Meta:
        model = Goods
        labels = {
            "name": "Имя",
            "text": "Комментарий",
        }
        exclude = [""]