from django import forms
from models import User, MediaItem, MediaHistory, Topics
#
# class UserForm(forms.ModelForm):
#     user_id = forms.CharField(max_length=20)
#     first_name = forms.CharField(widget=forms.HiddenInput())
#     last_name = forms.CharField(widget=forms.HiddenInput())
#