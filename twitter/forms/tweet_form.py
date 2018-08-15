# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

# from datetime import date

from twitter.models import Tweet

from django import forms


class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ('user', 'content',)

    # def clean_content(self):
    #     print("go where?")
    #     instance = self.cleaned_data.get('content')
    #     if len(instance) > 240 and len(instance) < 0:
    #         raise forms.ValidationError(
    #             'length is invalid!', code='invalid')
    #     return instance
