from django import forms
from registration.forms import RegistrationFormUniqueEmail
from .models import Algorithms
from django.core.exceptions import ValidationError

def file_size(value):
    limit = 20971520
    if value.size > limit:
        raise ValidationError('Arquivo muito grande. Tamanho máximo deve ser de 20MB.')

class UsuarioFriendsForm(RegistrationFormUniqueEmail):
    nickname = forms.CharField(required=False)
    company = forms.CharField(required=False)


class ExecutionForm(forms.Form):
    Algorithm = forms.ModelChoiceField(queryset=Algorithms.objects.all(),
                                       empty_label="---Selecione um algoritmo---",
                                       required=True,
                                       to_field_name="nameAlg",
                                       )
    Input = forms.FileField(required=False, validators=[file_size])


class ContactForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField()
