from django import forms
from django.utils.safestring import mark_safe

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle',
            'placeholder': 'Введите имя'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle',
            'placeholder': 'Введите email'
        })
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle',
            'placeholder': 'Текст вашего сообщения',
            'rows': 4
        })
    )
    agree = forms.BooleanField(
         label=mark_safe('Я принимаю <a href="https://policies.google.com/terms?hl=ru" target="_blank">Пользовательское соглашение</a>'),
        required=True
    )

