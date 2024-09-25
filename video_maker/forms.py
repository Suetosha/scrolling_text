from django import forms
from django.forms import ModelForm

from video_maker.models import VideoText


class TextForm(ModelForm):
    text = forms.CharField(label='Текст', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите текст для создания видео"}))

    class Meta:
        model = VideoText
        fields = ('text',)
