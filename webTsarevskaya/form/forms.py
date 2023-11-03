from .models import Feedback
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['surname', 'name', 'patronymic', 'email', 'height', 'weight', 'clothes_size', 'foot_size']

        widgets = {
            'surname': TextInput(attrs={
                'id': 'surname-input',
                'type': 'text',
                'placeholder': 'Фамилия'
            }),
            'name': TextInput(attrs={
                'id': 'name-input',
                'type': 'text',
                'placeholder': 'Имя'
            }),
            'patronymic': TextInput(attrs={
                'id': 'patronymic-input',
                'type': 'text',
                'placeholder': 'Отчество'
            }),
            'email': EmailInput(attrs={
                'id': 'email-input',
                'type': 'email',
                'placeholder': 'example@mail.ru'
            }),
            'height': NumberInput(attrs={
                'id': 'height-input',
                'type': 'number',
                'placeholder': 'Рост'
            }),
            'weight': NumberInput(attrs={
                'id': 'weight-input',
                'type': 'number',
                'placeholder': 'Вес'
            }),
            'clothes_size': Select(attrs={
                'id': 'clothes-size-select',
                'name': 'clothes'
            }),
            'foot_size': NumberInput(attrs={
                'id': 'foot-size-input',
                'type': 'number',
                'placeholder': 'Размер ноги'
            })
        }
